from config import ODBC_Connection
import json
import re
import requests
import pythoncom
import win32com.client
from datetime import datetime

class Common:
    def execute_query(query,fetch_one=False):
        odbc = ODBC_Connection()
        pgConn = odbc.pgConn
        cursor = pgConn.cursor()
        
        try:
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            
            if fetch_one:
                row = cursor.fetchone()
                result = dict(zip(columns,row)) if row else None
            else:
                result = []
                for row in cursor.fetchall():
                    result.append(dict(zip(columns,row)))
            return result
        finally:
            odbc.DBClose()
    
    def extract_strings_and_keys(total_summary):
        pattern = r'"([^"]*)"\[([^]]*)\]'
        matches = re.findall(pattern,total_summary)
        
        extracted_data = []
        for match in matches:
            string = match[0]
            key = match[1]
            extracted_data.append((string,key))
        
        return extracted_data
    
    def process_matches(key):
        pattern = r'([a-zA-Z])(\d{4})(\d{2})(\d{2})([a-zA-Z]+)(\d+)'
        matches = re.match(pattern,key)
    
        if matches:
            year = matches.group(2)
            month = matches.group(3)
            day = matches.group(4)
            pages = matches.group(5)
            seq = matches.group(6)
            datepublish = f"{year}-{month}-{day}"

            return {'datepublish': datepublish,'pages': pages,'seq': seq}
        else:
            return None

    def api_url(url,data):
        send_data = json.dumps(data)
        head_dict = {
            "Content-type": "application/json;charset='utf-8'",
            "Accept": "application/json"
        }
        response = requests.post(url,data=send_data,headers=head_dict,verify=False)
        
        try:
            retval = response.json()
        except json.JSONDecodeError:
            return None
        return retval

    def summary_log(path,data):
        with open(path,'a') as file:
            file.write(str(data)+'\n')
    
    def log_json(path,data):
        with open(path,'w') as json_file:
            json.dump(data,json_file,indent=4)

    def currentTime(type):
        datetimeNow = datetime.now()
        format_map = {
            'Ymd': '%Y%m%d',
            'Y-m-d': '%Y-%m-%d',
            'Y/m/d': '%Y/%m/%d',
            'HMS': '%H%M%S',
            'H:M:S': '%H:%M:%S',
            'YmdHMS': '%Y%m%d%H%M%S',
            'Y-m-d H:M:S': '%Y-%m-%d %H:%M:%S'
        }
        return datetimeNow.strftime(format_map.get(type,None))

    def sendMail(subject,body,receiver,sender='hotspot@digitimes.com'):
        pythoncom.CoInitialize()
        
        datetimeNow = datetime.now()
        # current_date = datetimeNow.strftime('%Y-%m-%d')
        current_date = datetimeNow.strftime('%Y-%m-%d %H:%M:%S')
        
        Mailer = win32com.client.Dispatch('Persits.MailSender')
        Mailer.Reset
        Mailer.Host = 'ms1.digitimes.com.tw'
        # Mailer.FromName = 'DIGITIMES Asia'
        Mailer.FromName = 'DIGITIMES HotSpot'
        Mailer.From = sender
        Mailer.AddAddress(receiver)
        Mailer.IsHTML = True
        Mailer.Subject = subject
        Mailer.Body = body
        Mailer.Charset = 'UTF-8'
        Mailer.TimeStamp = current_date
        Mailer.Queue = True
        Mailer.Send()
        
        Mailer = None