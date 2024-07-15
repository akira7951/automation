import requests
from datetime import datetime
from config import ODBC_Connection
from module import Common

def EmailList():
    query = (
        "select r.email, r.id from deng_registration r, deng_hotspot h "
        "where h.reg_id=r.id and r.verified='Y' and h.service ='geowatch' and h.out_date is null"
    )
    result = Common.execute_query(query)
    return result

def notify_mail(sub,content):
    notifyList = ['zoran@digitimes.com','lawrence.hu@digitimes.com']
    for notify in notifyList:
        Common.sendMail(sub,content,notify)

def get_content():
    url = 'https://apps.digitimes.com/cms/controls/emailpreview/PreviewEmail.asp?prtype=DH'
    headers = {
        'User-Agent': 'PythonAISummary'
    }
    response = requests.post(url,headers=headers)
    
    return response

def sendmail():
    datetimeNow = datetime.now()
    dateSubject = datetimeNow.strftime('%Y-%m-%d')
    run_date = datetimeNow.strftime('%Y-%m-%d')
    start_time = datetimeNow.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        pgConn = ODBC_Connection().pgConn
        cursor = pgConn.cursor()
        
        response = get_content()
        
        if response.status_code == 200:
            sub = f"Geowatch Weekly ({dateSubject})"
            logdate = datetimeNow.strftime('%Y/%m/%d')
            content = response.text
            content = content.replace('##logdate##',str(logdate))
            
            emailList = EmailList()
            for email in emailList:
                emailID = email['ID']
                content_r = content.replace('##memid##',emailID)
                Common.sendMail(sub,content_r,email['email'])
            
            query = (
                "select Max(news_date) from Webstatus where Webstat='Y'"
                "and run_time>(current_timestamp - interval '30 day') and run_time::date<current_date"
            )
            getResult = Common.execute_query(query,fetch_one=True)
            end_time = getResult['max']
            
            query = "select max(id) from hotspotstatus"
            getResult = Common.execute_query(query,fetch_one=True)
            maxID = getResult['max']+1
            
            query = (
                "insert into hotspotstatus "
                "(id,run_date,start_time,end_time,emails,service)"
                "values(?,?,?,?,?,?)"
            )
            insDict = [maxID,run_date,start_time,str(end_time),len(emailList),'geowatch']
            cursor.execute(query,insDict)
            pgConn.commit
        else:
            sub = 'Mail Out Error'
            msg = f"GeoWatch Weekly ({dateSubject}) Error code: {str(response.status_code)}"
            print(msg)
            notify_mail(sub,msg)
    except Exception as e:
            sub = 'Mail Out Error'
            msg = f"GeoWatch Weekly ({dateSubject}) Error code: {str(response.status_code)}"
            print(msg)
            notify_mail(sub,msg)

if __name__ == '__main__':
    sendmail()