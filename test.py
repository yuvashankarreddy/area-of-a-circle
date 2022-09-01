import requests
from bs4 import BeautifulSoup
import pandas

import sqlite3
def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS phone(NAME TEXT,PRICE TEXT)")
    print('table')
    conn.close()
def insert(dbname,values):
    conn =sqlite3.connect(dbname)
    insert_sql="INSERT INTO phone(NAME,PRICE)VALUES(?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()
def hotelinfo():
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM phone")
    data=cur.fetchall()
    for rec in data:
        print(rec)
    conn.close()
dbname='phone'
scraped_info_list=[]
connect(dbname)
url="https://www.newegg.com/global/in-en/SAMSUNG-Cell-Phones-Unlocked/BrandSubCat/ID-1077-2961"
req=requests.get(url)
content=req.content
soup=BeautifulSoup(content,"html.parser")
item_info=soup.find_all("div",{"class":"item-cell"})
for phone in item_info:
    phone_dict={}
    phone_dict["name"]=phone.find("a",{"class":"item-title"}).get_text()
    phone_dict["price"]=phone.find("li",{"class":"price-current"}).get_text()
    #print(phone_name+"===="+phone_price)
    scraped_info_list.append(phone_dict)
    insert(dbname,tuple(phone_dict.values()))

dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("phone.csv")
hotelinfo()
