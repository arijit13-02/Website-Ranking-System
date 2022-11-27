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
struct.geometry("600x300")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")

name=StringVar()

def dell():
    names=name.get().strip()
    cur.execute('select count(*) from information_schema.tables where table_schema = "wrs" && table_name like "'+username+'_'+names+'"')
    n=cur.fetchall()[0][0]
    if (n!=0):
        query="drop table "+username+"_"+names
        cur.execute(query)
        con.commit()
        os.system("rmdir /Q /S "+username+"_"+names)
        label=Label(struct,text="WEBSITE DELETED SUCCESSFULLY",bg="teal",fg="RED",font=("Times",18,"bold"))
        label.place(x=40,y=200)
        
    else:
        label=Label(struct,text="SUCH WEBSITE DOES NOT EXIST",bg="teal",fg="RED",font=("Times",18,"bold"))
        label.place(x=40,y=200)
        
        
    
        

label=Label(struct,text="Enter name of website",bg="teal",fg="white",font=("Times",18))
label.place(x=40,y=100)

enter=Entry(struct,font=("Times",18),textvar=name,width=20,bd=2,bg="white")
enter.place(x=300,y=100)


button=Button(struct,text="Submit",font=("Times",15,"bold"),width=18,bd=2,command=dell)
button.place(x=40,y=140)


struct.mainloop()
