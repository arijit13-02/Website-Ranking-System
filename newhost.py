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
struct.geometry("1400x500")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")

a_counter=0



name=StringVar()
keyword=StringVar()

def add():
    global a_counter
    if (a_counter==0):
        cur.execute('drop table '+username+'_'+names)
    cur.execute('create table '+username+'_'+names+'(keywords varchar(30))')
    con.commit()
    a=keywords.split(" ")
    for i in a:
        cur.execute('insert into '+username+'_'+names+' values("'+i+'")')
        con.commit()
    con.commit()
    global struct
    struct.destroy()
    struct=Tk()
    struct.geometry("1400x500")
    struct.title("WRS")
    label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
    label.place(x=40,y=40)
    struct.config(background="teal")
    label=Label(struct,text="Please follow these steps:",bg="teal",fg="white",font=("Times",18,"bold"))
    label.place(x=40,y=100)
    label=Label(struct,text="1. In the same directory create a folder with name as: yourUsername_websiteName",bg="teal",fg="white",font=("Times",18))
    label.place(x=40,y=140)
    label=Label(struct,text="2. Inside the folder post your materials, keeping the home page source code with the file name: yourUsername_websiteName_html.html",bg="teal",fg="white",font=("Times",18))
    label.place(x=40,y=180)
    label=Label(struct,text="3. The new Website has been added!",bg="teal",fg="white",font=("Times",18))
    label.place(x=40,y=220)
    
def damn():
    struct.destroy()
    os.system("py newhost.py "+username)

 

def addkeyword():
    global names
    global keywords
    names=name.get().strip()
    keywords=keyword.get().strip()
    cur.execute('select count(*) from information_schema.tables where table_schema = "wrs" && table_name like "'+username+'_'+names+'"')
    n=cur.fetchall()[0][0]
    if (n!=0):
        label=Label(struct,text="Such website already exists! Are you sure you want to overwrite it?",bg="teal",fg="white",font=("Times",18,"bold"))
        label.place(x=40,y=220)
        button=Button(struct,text="No Restart",font=("Times",15,"bold"),width=10,bd=2,command=damn)
        button.place(x=40,y=260)
        button=Button(struct,text="Continue",font=("Times",15,"bold"),width=10,bd=2,command=add)
        button.place(x=250,y=260)
    else:
        global a_counter
        a_counter=1
        add()
        
    
        

label=Label(struct,text="Enter name of website",bg="teal",fg="white",font=("Times",18))
label.place(x=40,y=100)

enter=Entry(struct,font=("Times",18),textvar=name,width=20,bd=2,bg="white")
enter.place(x=300,y=100)

label=Label(struct,text="Enter Keywords separated with spaces",bg="teal",fg="white",font=("Times",18))
label.place(x=40,y=140)

enter1=Entry(struct,font=("Times",18),textvar=keyword,width=70,bd=2,bg="white")
enter1.place(x=40,y=180)

button=Button(struct,text="Submit",font=("Times",15,"bold"),width=18,bd=2,command=addkeyword)
button.place(x=900,y=180)


struct.mainloop()
