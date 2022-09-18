from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import csv 

PATH = "chromedriver.exe"
d = webdriver.Chrome(PATH)
Table_dict={}
templist=[]
r=1
for i in range(1,119):
    d.get("https://pt.kle.cz/en_US/index-an.html")
    d.maximize_window()
    elem = d.find_element(By.NAME,i)
    elem.send_keys(Keys.RETURN)
    while(1): 
        try:
            data_key = d.find_element(By.XPATH,'//*[@id="atom"]/tbody/tr['+str(r)+']/th').text 
            if(r<8):
                data_value = d.find_element(By.XPATH,'//*[@id="atom"]/tbody/tr['+str(r)+']/td/a').text 
            else:
                data_value = d.find_element(By.XPATH,'//*[@id="atom"]/tbody/tr['+str(r)+']/td/div').text
            Table_dict[data_key] = data_value
            r+=1
        except NoSuchElementException: 
            break
    r=1
    templist.append(Table_dict)
    df = pd.DataFrame(templist)
    Table_dict={}
df.to_csv('table.csv')
time.sleep(1)
d.quit()
 
