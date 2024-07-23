import re
import requests
from config import Common
from config import ODBC32
from datetime import datetime

def extract_strings_and_keys(total_summary):
    pattern = r'"([^"]*)"\[([^]]*)\]'
    matches = re.findall(pattern,total_summary)
    
    extracted_data = []
    for match in matches:
        string = match[0]
        key = match[1]
        extracted_data.append((string,key))
    
    return extracted_data

def replace_summary(total_summary):
    extracted_data = extract_strings_and_keys(total_summary)
    modified_str = total_summary
    
    for data in extracted_data:
        original_str = f'"{data[0]}"[{data[1]}]'
        # link = f"<a href='https://www.digitimes.com/news/{data[1]}.html?chid=2&utm_source=newsletter&utm_medium=email&utm_campaign=geowatch&utm_id=geowatch&utm_content=summary'>{data[0]}</a>"
        # link = link.replace("'",'"')

        link = f"<a href='https://www.digitimes.com/news/{data[1]}.html?mod=2&utm_source=newsletter&utm_medium=email&utm_campaign=geowatch&utm_id=geowatch&utm_content=summary'>"
        link = link.replace("'",'"')
        last = f"{data[0]}</a>"
        link = link+last

        modified_str = re.sub(re.escape(original_str),link,modified_str)
    
    # finall = modified_str.replace('.;','; ')
    final = re.sub(r'\.\s*;','; ',modified_str)
    return final

def get_content():
    url = 'https://apps.digitimes.com/cms/controls/emailpreview/PreviewEmail.asp?prtype=DH'
    headers = {
        'User-Agent': 'PythonAISummary'
    }
    response = requests.post(url,headers=headers)
    
    return response

def get_summary(cursor):
    query = (
            "Select ch.datePublish, ch.pages, ch.seq, ch.subject, ch.body, "
            "(b.cnt/extract(epoch from (current_timestamp - e.comptime))/3600) perh, b.cnt, e.comptime "
            "From deng_contenthuman ch, deng_newstranslator e, (Select r.datepublish, r.pages, r.seq "
            "From deng_contenthuman ch, deng_newstranslator e, relTags r "
            "Where r.datePublish = ch.datePublish And r.pages = ch.pages And r.seq = ch.seq and "
            "r.datePublish = e.datePublish And r.pages = e.pages And r.seq = e.seq and "
            "e.complete = 'Y' and e.comptime::date<current_date and r.id in (select tagid from topictags t where id=628) "
            "group by r.datepublish, r.pages, r.seq "
            "Union "
            "Select r.datepublish, r.pages, r.seq "
            "From deng_contenthuman ch, deng_newstranslator e, relTopic r "
            "Where r.datePublish = ch.datePublish And r.pages = ch.pages And r.seq = ch.seq and "
            "r.datePublish = e.datePublish And r.pages = e.pages And r.seq = e.seq and "
            "e.complete = 'Y' and e.comptime::date<current_date and r.id=628 "
            "group by r.datepublish, r.pages, r.seq) r left join "
            "(select datepublish,pages,seq, count(1) cnt from (select datepublish,pages,seq,id from deng_monitormem dm "
            "union "
            "select datepublish,pages,seq,id from deng_monitormem_his dmh where effectdate >(current_timestamp - interval '60 day') "
            "group by datepublish,pages,seq,id) m, "
            "(select * from deng_registration dr where pay_seq>10) r "
            "where m.id=r.id "
            "group by datepublish,pages,seq) b on r.datepublish=b.datepublish and r.pages=b.pages and r.seq=b.seq "
            "Where r.datePublish = ch.datePublish And r.pages = ch.pages And r.seq = ch.seq and "
            "r.datePublish = e.datePublish And r.pages = e.pages And r.seq = e.seq "
            "and e.comptime>(Select end_time from hotspotstatus where id=(Select Max(ID) from hotspotstatus where service='geowatch')) "
            "and e.comptime<=(Select Max(news_date) from Webstatus where Webstat='Y' "
            "and run_time>(current_timestamp - interval '30 day') and run_time::date<current_date) "
            "order by perh desc limit 5"
    )
    cursor.execute(query)
    
    selectData = []
    for row in cursor.fetchall():
        selectData.append(dict(zip([desc[0] for desc in cursor.description],row)))
    
    return selectData

def ErrorMail(sub,msg):
    sub = f"Error Message: {sub}"
    notifyList = [
        'zoran@digitimes.com',
        'lawrence.hu@digitimes.com'
    ]
    for notify in notifyList:
        Common.sendMail(sub,msg,notify)

def run_aisummary():
    sub = 'AI Summary'
    
    try:
        odbc = ODBC32()
        pgConn = odbc.pgConn32
        cursor = pgConn.cursor()
        
        selectData = get_summary(cursor)
        
        comb = []
        for item in selectData:
            originalDate = datetime.strptime(str(item['datepublish']),'%Y-%m-%d')
            datepublish = str(originalDate.strftime('%Y%m%d'))
            comb.append(
                {
                    'key': f"a{datepublish}{item['pages']}{str(item['seq'])}",
                    'subject': item['subject'],
                    'body': item['body']
                }
            )
        
        if comb == []:
            msg = 'Error: query'
            ErrorMail(sub,msg)
            exit()
        
        url = 'http://xxx.xxx.xxx.xxx:xxxx/summary' # hide
        result = None
        
        while True:
            result = Common.api_url(url,{'data': comb})
            if 'error' not in result or result.get('error') != 'incomplete length':
                break
            else:
                print(result)
        
        if not result or 'data' not in result:
            msg = f"Error from {url}"
            ErrorMail(sub,msg)
            exit()
        else:
            result = result['data']
        
        total_summary = replace_summary(result[len(result)-1]['total_summary'])
        query = "update deng_newssummary set emldsp = 'N' where emldsp = 'Y'"
        cursor.execute(query)
        
        current_date = Common.currentTime('Y-m-d')
        current_datetime = Common.currentTime('Y-m-d H:M:S')
        
        query = (
            "insert into deng_newssummary "
            "(datepublish,pages,seq,userid,moddate,emldsp,emlpos,emlname,summary)"
            "values(?,?,?,?,?,?,?,?,?)"
        )
        headDict = [current_date,'XY',500,None,current_datetime,'Y',0,'geowatch',total_summary]
        cursor.execute(query,headDict)
        
        dataDict = {d['url'].split('/')[-1].split('.')[0]: d['summary'] for d in result if 'summary' in d}
        for item in comb:
            key = item['key']
            if key in dataDict:
                item['body'] = dataDict[key]
        
        for i,item in enumerate(comb):
            matches = Common.process_matches(item['key'])
            insDict = [str(matches['datepublish']),matches['pages'],int(matches['seq']),None,current_datetime,'Y',i+1,'geowatch',item['body']]
            cursor.execute(query,insDict)
        
        pgConn.commit()
    except Exception as e:
        msg = f"{sub} Error: {str(e)}"
        ErrorMail(sub,msg)
        print(msg)
    finally:
        odbc.DBClose()

if __name__ == '__main__':
    run_aisummary()
