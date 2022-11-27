import requests,webbrowser
import os
import sys
from bs4 import BeautifulSoup
from tkinter import *

import mysql.connector as mycon
con = mycon.connect(host='localhost', user='root', password = "1234")
cur = con.cursor()
cur.execute("create database if not exists wrs")
cur.execute("use wrs")
username=str(sys.argv[1])

struct=Tk()
struct.geometry("800x330")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")

cur.execute('select count(*) from information_schema.tables where table_schema = "wrs" && table_name like "'+username+'%"')
n=cur.fetchall()[0][0]
if (n==0):
    label=Label(struct,text="The user has currently not hosted any websites!",bg="teal",fg="white",font=("Times",18,"bold"))
    label.place(x=40,y=140)
else:
    label=Label(struct,text="Websites",bg="teal",fg="white",font=("Times",18,"bold"))
    label.place(x=40,y=140)
    label=Label(struct,text="Keywords",bg="teal",fg="white",font=("Times",18,"bold"))
    label.place(x=300,y=140)
    q="select table_name from information_schema.tables where table_name like '"+username+"%'"
    cur.execute(q)
    a=cur.fetchall()
    yy=180
    yyy=180
    for i in range(n):    
        website=a[i][0]
        corewebsite=website.split("_")[1]
        label=Label(struct,text=corewebsite,bg="teal",fg="white",font=("Times",18,))
        label.place(x=40,y=yy)
        query="select * from "+website
        cur.execute(query)
        aa=cur.fetchall()
        
        for j in range(len(aa)):
            label=Label(struct,text=aa[j][0],bg="teal",fg="white",font=("Times",18,))
            label.place(x=300,y=yyy)
            yyy+=40
        yy=yyy
    struct.geometry("600x"+str(yy))
        
struct.mainloop()
