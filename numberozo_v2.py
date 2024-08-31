import requests
import os
import pandas as pd
from tqdm import tqdm 
import json

tblm={'SA':966,'EG':20,'KW':965,'AE':971,'DZ':213,'MA':212,'TN':216,'IQ':964,'BH':973,'PS':970,'LB':961
  ,'YE':967,'SD':249,'OM':968,'QA':974,'LY':218,'SY':963,'JO':962}

cou=open("country.txt",'r')
country=cou.readline().strip()
cou.close()
rFiles=[]
arr = os.listdir()
for g in arr:
    if g[-4:]=='.txt' and g!="country.txt" :
        rFiles.append(g)
f=open( rFiles[0] , encoding='utf-8' )
NAME=[]
for p in f:
    ncf=p.strip()
    NAME.append(ncf)
f.close()
colum = {'search':[],'phone':[],'name':[]}

print('\n'*10)
l=1
with tqdm(total=len(NAME),desc ="Download progress") as pbar:
    try:
        for nm in NAME:
            url=f"https://numberozo.com/api/php/api-name77.php?num={nm}&country={country}&country_code={tblm[country]}&id=a5DytbOC4XwHbRq1RUZ9dH6q2i65gMI2lFwn9r/0NBU=&format=json"
            r = requests.get(url, headers={"User-Agent": "XY"})
            r=r.json()
            rayyData=r[0]['data']
            lenData=len(r[0]['data'])
            for dta in rayyData:
                try:
                    colum['name'].append(dta['name'])
                except:
                    colum['name'].append(None)
                try:
                    colum['phone'].append(dta['phone'])
                except:
                    colum['phone'].append(None)
                colum['search'].append(nm)  
            pbar.update(1)
            if len(colum['name'])>=50000:
                nemfile=rFiles[0].split(".")
                data=pd.DataFrame(colum)
                data.to_excel(str(nemfile[0])+str(l)+'.xlsx',sheet_name='sheet1',index=False)
                colum = {'search':[],'phone':[],'name':[]}
                l+=1
    except:
        pbar.update(1)
        pass

nemfile=rFiles[0].split(".")
data=pd.DataFrame(colum)
data.to_excel(str(nemfile[0])+'_'+str(l)+'.xlsx',sheet_name='sheet1',index=False)