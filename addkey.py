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
website=str(sys.argv[2])

struct=Tk()
struct.geometry("500x380")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")

name=StringVar()


def add():
    a=name.get().strip()
    a=a.split(" ")
    for i in a:
        cur.execute('insert into '+username+'_'+website+' values("'+i+'")')
        con.commit()
    con.commit()
    label=Label(struct,text="KEYWORDS ADDED SUCCESSFULLY!",bg="teal",fg="RED",font=("Times",18,"bold"))
    label.place(x=40,y=260)
    enter.config(state= "disabled")   

label=Label(struct,text="Enter keywords seprated by spaces",bg="teal",fg="white",font=("Times",18))
label.place(x=40,y=100)

enter=Entry(struct,font=("Times",18),textvar=name,width=30,bd=2,bg="white")
enter.place(x=40,y=150)


button=Button(struct,text="Submit",font=("Times",15,"bold"),width=20,bd=2,command=add)
button.place(x=40,y=200)


struct.mainloop()
