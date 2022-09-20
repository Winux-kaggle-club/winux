import time
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
global list_keys
list_keys=[]




# Function to fetch data
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




d.get("https://periodic.winuxdroid.com")
d.find_element(By.ID,"element1").click()
for i in range(1,119):
  d.get(f"https://periodic.winuxdroid.com/element.html?num={i}")
  time.sleep(2)
  for j in div_list:
    if(j==3):
      fetch(6,j,1)
    else:
      fetch(7,j,1)
  templist.append(Table_dict)
  Table_dict={}       





# If we don't know all the elements have same number of keys we can use this approach
# z=0
# for i in templist:
#   for keys in templist[z]:
#     if(keys not in list_keys):
#       list_keys.append(keys)
#   z+=1        




for keys in templist[0]:
  list_keys.append(keys)
with open("data.csv",'w') as f:
    for i in list_keys:
        f.write(i+",")
    f.write("\n")
    z=0
    for i in templist:
      for keys in templist[z]:
        if "," in templist[z][keys]:
          f.write(f'"{templist[z][keys]}"')
        else:
          f.write(templist[z][keys]+",")
      f.write("\n")
      z+=1  
    f.close()


# Peace Out    
d.quit()