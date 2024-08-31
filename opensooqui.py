from requests_html import HTMLSession
import requests
import pandas as pd
import time
import sys
import random
from tqdm import tqdm
from datetime import timedelta,date

#====================== function get date ===================
def return_date(pr):
    pr1=pr.split(' ')
    prd=pr.split('-')
    if any(e in pr1 for e in ['minutes','ago','hour','Now']):
        return date.today().strftime('%d-%m-%Y')
    elif any(e in pr1 for e in ['Yesterday']):
        return (date.today() + timedelta(days=-1)).strftime('%d-%m-%Y')
    elif len(prd)==3:
        return pr1[0]
    else:
        return ''
#====================== function get num phone ===================
def num_phone(id):
    url = f"https://sa.opensooq.com/v2.1/posts/{id}"
    querystring = {"fields":"local_phone,phone"}
    payload = ""
    headers = {
        "authority": "sa.opensooq.com",
        "accept": "*/*",
        "accept-language": "ar",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdDAiOjE2ODg5OTQ3NzIsImF1ZCI6ImRlc2t0b3AiLCJzdWIiOiJmNDExOTFlMS1hOWYyLTRhM2MtYjM3ZS03MjRiZjAwYjhlMGEiLCJybmQiOiIxMjAxNjEwODA4MTI2IiwiZXhwIjoxNjg5OTY1NDk4fQ.8Pe_e-bxJoLT500GLU3a8XIfhnJ4yDN2Vey9UxwpUg8",
        "cookie": "NEXT_LOCALE=ar; source=desktop; auth_v2=^%^7B^%^22deviceUUID^%^22^%^3A^%^22f41191e1-a9f2-4a3c-b37e-724bf00b8e0a^%^22^%^2C^%^22t^%^22^%^3A1688994772^%^2C^%^22k^%^22^%^3A^%^227186a03f9ffce232ed6262250cc79bd99aba195d7402888b703b83dc3f9af119^%^22^%^7D; FIREBASE_FCM_TOKEN=FIREBASE_CLICKED_NO; _ga=GA1.1.1162529453.1688994814; ecountry=sa; _ga=GA1.3.1162529453.1688994814; _cc_id=8ece9b93207c756215c71cb549a3d78; _clck=1hs3k0r^|2^|fdh^|0^|1286; _pbjs_userid_consent_data=3524755945110770; _gid=GA1.3.1617829343.1689963957; panoramaId_expiry=1690568714389; panoramaId=e4e36af133ff204426842f74b00716d53938d5a947f8d4388a9cfb7a44811031; panoramaIdType=panoIndiv; cto_bundle=FI_Qf19xREVodzBOZjlFSFVPbkU0UVk4MWhvZmY3WTVMNzhqNTZ0UmtRTFVsTEZwbGVJY1k0Y1kxWjJ0Vjc3NzRBcE9zYjhpbVhPQiUyQnN6MkxRWmRqc3JuRmN2bkFlWGdWM3gzRFQzRDlBNUhsVE5YRkVXY3hqbjhhM3VtSnU0cU1OeTN5V0ZTbDV3MFI2JTJGWjFpbkc0ZnFKd2RBJTNEJTNE; userInfo=^%^7B^%^7D; _col_uuid=d2b87ad5-1afb-44a1-8644-79b596d152d6-h0k8; __gads=ID=ec38a3e1a4f27470:T=1688994828:RT=1689964870:S=ALNI_MZpCBKZ4OmZolG8XIv4NAfBU1JmHg; __gpi=UID=00000c65c9f1ff8f:T=1688994828:RT=1689964870:S=ALNI_MYTKt4w7imvEy0Fna3M09qv_Dh8YQ; _clsk=t50g3^|1689965150792^|3^|1^|q.clarity.ms/collect; _gat_UA-3883661-1=1; _ga_GXHH539B0K=GS1.1.1689963956.2.0.1689965195.0.0.0; session=^%^7B^%^22id^%^22^%^3A^%^22f41191e1a9f2-4a3c3a9dbcf4-1641-417a-825e-552a281f8f36^%^22^%^2C^%^22startedAt^%^22^%^3A1689965197987^%^7D",
        "country": "sa",
        "referer": "https://sa.opensooq.com/ar/^%^D8^%^AD^%^D8^%^B1^%^D8^%^A7^%^D8^%^AC-^%^D8^%^A7^%^D9^%^84^%^D8^%^B3^%^D9^%^8A^%^D8^%^A7^%^D8^%^B1^%^D8^%^A7^%^D8^%^AA/^%^D8^%^B3^%^D9^%^8A^%^D8^%^A7^%^D8^%^B1^%^D8^%^A7^%^D8^%^AA-^%^D9^%^84^%^D9^%^84^%^D8^%^A8^%^D9^%^8A^%^D8^%^B9/^%^D8^%^AA^%^D9^%^88^%^D9^%^8A^%^D9^%^88^%^D8^%^AA^%^D8^%^A7",
        "release-version": "9.4.02",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "session-id": "f41191e1a9f2-4a3c3a9dbcf4-1641-417a-825e-552a281f8f36",
        "source": "desktop",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "x-domain-theme": "opensooq",
        "x-tracking-uuid": "f41191e1-a9f2-4a3c-b37e-724bf00b8e0a"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()["phone"]
#====================== config.txt ====================================

try:
    f = open("config.txt", encoding='utf-8' )
    url=f.readline().split('URL :')[1].strip().split('?pageNum=')[0]
    first_number=int(f.readline().split('FIRST_PAGEF_NUMBER :')[1].strip())
    last_number=int(f.readline().split('LAST_PAGE_NUMBER :')[1].strip())
    times=float(f.readline().split('TIME(s) :')[1].strip())
    f.close()
except:
    print('\n'*5,'Make sure that the .confg.txt file is written correctly')
    time.sleep(8)
    sys.exit()

colum = {'Titel':[],'Phone':[],'Date':[],'Type':[],'City':[],'Page':[]}
session = HTMLSession()

print('\n'*5)

with tqdm(total=last_number,desc ="Download progress") as pbar:
    for i_this in range(first_number,last_number+1):
        try:
            r = session.get(f'{url}?page={i_this}')
            autho = r.html.xpath('//*[@id="listing_posts"]/div')
            for author in autho:
                try:                      
                    colum['Date'].append(return_date(author.xpath('//span')[0].text))
                except:
                    colum['Date'].append(None)
                try:
                    colum['Phone'].append(num_phone(author.xpath('//a/@href')[0].split('/')[3]))
                except:
                    colum['Phone'].append(None)
                try:
                    colum['Titel'].append(author.xpath('//a/div[2]/div[1]/h2')[0].text)
                except:
                    colum['Titel'].append(None)   
                try:
                    colum['Type'].append(author.xpath('//a/div[2]/div[2]')[0].text)
                except:
                    colum['Type'].append(None)  
                try:
                    colum['City'].append(author.xpath('//a/div[2]/div[3]/div/span')[0].text)
                except:
                    colum['City'].append(None)
                try:
                    colum['Page'].append(i_this)
                except:
                    colum['Page'].append(None)
            time.sleep(times)
            pbar.update(1)
        except:
            continue
            pbar.update(1)

data=pd.DataFrame(colum)
data.to_excel(str(random.randint(0,99999))+'.xlsx',sheet_name='sheet1',index=False) 