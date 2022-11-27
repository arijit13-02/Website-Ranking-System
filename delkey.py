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
struct.geometry("1400x500")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")

name=StringVar()

def add():
    keyw=enter.get().strip().split(" ")
    for key in keyw:
        dequery="delete from "+username+"_"+website+" where keywords='"+key+"'"
        cur.execute(dequery)
        con.commit()
    enter.config(state= "disabled")  
    label=Label(struct,text="KEYWORDS SUCCESSFULLY REMOVED FROM THE WEBSITE:",bg="teal",fg="red",font=("Times",18,"bold"))
    label.place(x=600,y=250)

label=Label(struct,text="KEYWORDS PRESENT IN THE WEBSITE:",bg="teal",fg="white",font=("Times",18,"bold"))
label.place(x=40,y=100)
query="select * from "+username+"_"+website
cur.execute(query)
a=cur.fetchall()
yy=140
for i in range(len(a)):
    label=Label(struct,text=a[i][0],bg="teal",fg="white",font=("Times",18,))
    label.place(x=40,y=yy)
    yy+=40
struct.geometry("1300x"+str(yy))
label=Label(struct,text="Enter Keywords you want to delete separated by space",bg="teal",fg="white",font=("Times",18))
label.place(x=600,y=100)

enter=Entry(struct,font=("Times",18),textvar=name,width=50,bd=2,bg="white")
enter.place(x=600,y=140)

button=Button(struct,text="Submit",font=("Times",15,"bold"),width=20,bd=2,command=add)
button.place(x=600,y=200)


struct.mainloop()
