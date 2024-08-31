from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random
import sys
import openpyxl
from openpyxl import load_workbook
import pandas as pd
import keyboard
import ast
from selenium.webdriver.chrome.options import Options
import json

file = open('newurl66.txt', "r")
lst=file.read()
lst = ast.literal_eval(lst)
lst=list(set(lst))
print(len(lst))

service = Service(executable_path='./chromedriver.exe')
options = Options()
options.add_argument('--no-sandbox')
# options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--incognito")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
driver = webdriver.Chrome(service=service, options=options)
        
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
})
er=0
kr=0
listobject=[]
for url in lst:
    try:
        driver.get(url)
        colum={}
        lnk=driver.find_elements(by=By.XPATH,value='//*[@id="primary"]/div[1]')[0].text
        colum["Track"]=lnk
    
        mrc=driver.find_elements(by=By.XPATH,value='//*[@id="pdpMain"]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span')[0].text
        colum["Type"]=mrc
  
        title=driver.find_elements(by=By.XPATH,value='//*[@id="pdpMain"]/div[1]/div[2]/div[2]/div[1]/h1/span')[0].text
        colum["Title"]=title

        price=driver.find_elements(by=By.XPATH,value='//*[@id="price-block"]/div[1]/span')[0].text
        colum["Price"]=price
    
        list_p=driver.find_elements(by=By.XPATH,value='//*[@id="product-content"]/div[3]/ul/li')
        k=1
        for einp in list_p:
            colum[f"Size{k}"]=einp.text.replace('\n',' | ')
            k+=1
     
        textt=driver.find_elements(by=By.CLASS_NAME,value='tabs-content')[0]
        colum["Details"]=textt.text
        time.sleep(2)
        driver.execute_script('document.getElementsByClassName("tab-title")[1].click()')
        text2=driver.find_elements(by=By.CLASS_NAME,value='tabs-content')[0]
        colum["Ingredients"]=text2.text
        photo_p=driver.find_elements(by=By.CLASS_NAME,value='thumb')
        k=1
        for einf in photo_p:
            colum[f"Photo{k}"]="https://www.sephora.sa/"+einf.find_element(by=By.TAG_NAME,value='a').get_attribute('data-zoom-image').replace('https://www.sephora.sa/','')
            k+=1
        listobject.append(colum)

        print(kr)
        kr+=1
        lst.remove(url)

            
    except:   
        er+=1
        if er==10:
            break

    


jsonString = json.dumps(listobject)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()   

f = open("newurl.txt", "w")
f.write(str(lst))
f.close()