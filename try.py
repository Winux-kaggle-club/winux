import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



PATH = "chromedriver.exe"
d = webdriver.Chrome(PATH)
templist=[]
div_list=[3,13,9]
d.maximize_window()
global Table_dict
Table_dict={}




def fetch(x,j,k):
  for l in range(x):
    try:
      if(k==1 and j==3):
        data_key="Symbol"
        data_value=d.find_element(By.ID,"resultSymbolInner").text
        Table_dict[data_key] = data_value
      data_key=d.find_element(By.XPATH,f'//*[@class="masonry"]/div[{j}]/div[1]/div[{k}]').text
      data_value=d.find_element(By.XPATH,f'//*[@class="masonry"]/div[{j}]/div[1]/div[{k+1}]').text         
      Table_dict[data_key] = data_value
      k+=2    
    except NoSuchElementException: 
      break  




for i in range(1,4):
  d.get(f"https://periodic.winuxdroid.com/element.html?num={i}")
  time.sleep(3)
  for j in div_list:
    if(j==3):
      fetch(6,j,1)
    else:
      fetch(7,j,1)
  templist.append(Table_dict)
  df = pd.DataFrame(templist)
  Table_dict={}       




print(templist)
df.to_csv('table.csv')
time.sleep(1)    
d.quit()