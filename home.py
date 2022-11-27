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
struct.geometry("800x500")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")


label=Label(struct,text="USER DASHBOARD:",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=50,y=100)

def error404():
    os.system("py error404.py")

button=Button(struct,text="Website Creation Portal",font=("Times",15,"bold"),width=25,bd=2,command=error404)
button.place(x=450,y=160)

def statprev():
    os.system("py statprev.py"+" "+sys.argv[1])

def newhost():
    os.system("py newhost.py"+" "+sys.argv[1])

def delhost():
    os.system("py delhost.py"+" "+sys.argv[1])

def keyword():
    os.system("py keyword.py"+" "+sys.argv[1])

button=Button(struct,text="Status of previous hosted websites",font=("Times",15,"bold"),width=25,bd=2,command=statprev)
button.place(x=50,y=160)

button=Button(struct,text="Host New Websites",font=("Times",15,"bold"),width=25,bd=2,command=newhost)
button.place(x=50,y=260)

button=Button(struct,text="Keyword Suggestion Portal",font=("Times",15,"bold"),width=25,bd=2,command=error404)
button.place(x=450,y=260)

button=Button(struct,text="Delete Webstites",font=("Times",15,"bold"),width=25,bd=2,command=delhost)
button.place(x=50,y=360)


button=Button(struct,text="Edit Keywords",font=("Times",15,"bold"),width=25,bd=2,command=keyword)
button.place(x=450,y=360)

struct.mainloop()