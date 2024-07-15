from module import Common
from datetime import datetime
import requests
import time

def get_content():
    url = 'https://apps.digitimes.com/cms/controls/emailpreview/PreviewEmail.asp?prtype=DH'
    headers = {
        'User-Agent': 'PythonAISummary'
    }
    response = requests.post(url,headers=headers)
    
    return response

def notify_mail(sub,content):
    notifyList = ['zoran@digitimes.com','lawrence.hu@digitimes.com']
    for notify in notifyList:
        Common.sendMail(sub,content,notify)

def draftMai():
    sendList = [
        'judy.lin@digitimes.com',
        'tony.chang@digitimes.com',
        'joyce.siow@digitimes.com',
        'joe.tsai@digitimes.com',
        'vyra.wu@digitimes.com',
        'rod.chang@digitimes.com',
        'jeff.chi@digitimes.com',
        'alan.hsu@digitimes.com',
        'misha.lu@digitimes.com',
        'zocp@hotmail.com',
        'zocp@yahoo.com',
        'zoran.pavlovski@gmail.com',
        'giayucyt@gmail.com',
        'pets5532@hotmail.com',
        'pets5532@yahoo.com',
        'book.fu@digitimes.com',
        'chloe.tu@digitimes.com',
        'irene.cheng@digitimes.com',
        'jay.liang@digitimes.com',
        'zoran@digitimes.com',
        'lawrence.hu@digitimes.com'
    ]
    
    try:
        datetimeNow = datetime.now()
        dateSubject = datetimeNow.strftime('%Y-%m-%d')
        
        response = get_content()
        
        if response.status_code == 200:
            # sub = f"GeoWatch {str(dateSubject)} draft for review"
            sub = f"GeoWatch Weekly draft ({dateSubject})"
            content = response.text
            
            emails_per_second = 3

            for list in sendList:
                Common.sendMail(sub,content,list)
                time.sleep(1/emails_per_second)
        else:
            sub = 'Send Mail Error'
            msg = f"GeoWatch Weekly draft ({dateSubject}) Error code: {str(response.status_code)}"
            notify_mail(sub,msg)
    except Exception as e:
        sub = 'Send Mail Error'
        msg = f"GeoWatch Weekly draft ({dateSubject}) Error Message: {str(e)}"
        notify_mail(sub,msg)

if __name__ == '__main__':
    draftMai()