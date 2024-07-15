from config import ODBC_Connection
from module import Common
from pianosdk import Client
from datetime import datetime
import json

def determine_wstatus(type,event):
    wstatus = 'O'
    # if type == 'user_updated':
    #     if event in ('piano_id_user_custom_fields_updated','user_updated'):
    #         wstatus = 'D'
    if type == 'subscription_renewal':
        if event in ('subscription_auto_renewed',):
            wstatus = 'D'
        elif event in ('subscription_manually_renewed'):
            wstatus = 'C'
        elif event in ('subscription_auto_renewed_failure','subscription_auto_renewed_auth_failure'):
            wstatus = 'F'
    return wstatus

def ErrorMail(sub,msg):
    sub = f"Error Message: {sub}"
    notifyList = [
        'zoran@digitimes.com',
        'lawrence.hu@digitimes.com'
    ]
    for notify in notifyList:
        Common.sendMail(sub,msg,notify)

def webhook():
    subject = 'Webhook'
    
    try:
        odbc = ODBC_Connection()
        pgConn = odbc.pgConn
        cursor = pgConn.cursor()
        
        apiHost = 'https://api-ap.piano.io/api/v3'
        apiToken = '' # hide Token
        privateKey = '' # hide privateKey
        
        query = "select webhook,webhookid from deng_pianowebhooks where wstatus = 'N'"
        getResult = Common.execute_query(query)
        
        if not getResult:
            msg = 'no data'
            print(msg)
        else:
            datetimeNow = datetime.now()
            current_datetime = datetimeNow.strftime('%Y-%m-%d %H:%M:%S')
            client = Client(api_host=apiHost,api_token=apiToken,private_key=privateKey)
        
            for item in getResult:
                webhook = item['webhook']
                webhookid = item['webhookid']
                
                response = client.parse_webhook_data(webhook)
                
                if not response:
                    msg = f"{str(current_datetime)} pianosdk returned error"
                    ErrorMail(subject,msg)
                    exit()
                else:
                    responseDict = vars(response)
                
                type = responseDict['type']
                event = responseDict['event']
                uid = responseDict['uid']
                
                json_payload = json.dumps(responseDict)
                wstatus = determine_wstatus(type,event)
                
                query = (
                    "update deng_pianowebhooks "
                    f"set uid = '{uid}', htype = '{type}', hevent = '{event}', json_payload = '{json_payload}', wstatus = '{wstatus}' "
                    f"where webhookid = {webhookid}"
                )
                cursor.execute(query)
                pgConn.commit()
    except Exception as e:
        msg = 'webhook error: '+str(e)
        ErrorMail(subject,msg)
    finally:
        odbc.DBClose()

if __name__ == '__main__':
    webhook()