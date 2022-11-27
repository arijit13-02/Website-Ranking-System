import requests,webbrowser
from bs4 import BeautifulSoup
from tkinter import *
import os
import sys


import mysql.connector as mycon
con = mycon.connect(host='localhost', user='root', password = "1234")
cur = con.cursor()
cur.execute("create database if not exists wrs")
cur.execute("use wrs")

p=1
ranked=[]

struct=Tk()
struct.geometry("350x250")
struct.title("My Search Engine")
label=Label(struct,text="Personal Search Engine",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")
text=StringVar()
yy=280
def disp0():
    q="start " + ranked[0]+"\\"+ranked[0]+"_html.html"
    os.system(q)

def disp1():
    q="start " + ranked[1]+"\\"+ranked[1]+"_html.html"
    os.system(q)
    
def disp2():
    q="start " + ranked[2]+"\\"+ranked[2]+"_html.html"
    os.system(q)

def search():
    enter.config(state= "disabled")
    keywords=text.get().split(" ")
    q="show tables where tables_in_wrs NOT LIKE 'users'"
    cur.execute(q)
    websites=cur.fetchall()
    key=[]
    web=[]
    for i in range(len(websites)):
        core=websites[i][0]
        web.append(core)
        q="select * from "+core
        cur.execute(q)
        key.append(cur.fetchall())
    rank=[]
    count=0
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j][0] in keywords:
                count+=1
        rank.append(count)
        count=0
    global ranked
    for i in range(len(web)):
        if max(rank)==0:
            break
        ranked.append(web[rank.index(max(rank))])
        rank.remove(max(rank))
        web.remove(ranked[i])
    global p
    global yy
    label=Label(struct,text="SEARCH RESULTS:",bg="teal",fg="white",font=("Times",15,"bold"))
    label.place(x=50,y=230)
    i=0
    if len(ranked)==0:
        label=Label(struct,text="NO RESULTS FOUND!",bg="teal",fg="white",font=("Times",15,"bold"))
        label.place(x=50,y=yy)
    if len(ranked)==1:
        button=Button(struct,text="Website "+ (str(i+1)),font=("Times",10,"bold"),width=30,bd=2,command=disp0)
        button.place(x=50,y=yy)
    if len(ranked)==2:
        button=Button(struct,text="Website "+ (str(i+1)),font=("Times",10,"bold"),width=30,bd=2,command=disp0)
        button.place(x=50,y=yy)
        yy=yy+40
        button=Button(struct,text="Website "+ (str(i+2)),font=("Times",10,"bold"),width=30,bd=2,command=disp1)
        button.place(x=50,y=yy)
        yy=yy+40
    if len(ranked)>2:
        button=Button(struct,text="Website "+ (str(i+1)),font=("Times",10,"bold"),width=30,bd=2,command=disp0)
        button.place(x=50,y=yy)
        yy=yy+40
        button=Button(struct,text="Website "+ (str(i+2)),font=("Times",10,"bold"),width=30,bd=2,command=disp1)
        button.place(x=50,y=yy)
        yy=yy+40
        button=Button(struct,text="Website "+ (str(i+3)),font=("Times",10,"bold"),width=30,bd=2,command=disp2)
        button.place(x=50,y=yy)
  
    struct.geometry("350x"+str(yy+50))


        
label=Label(struct,text="Enter here to search",bg="teal",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)
enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=50,y=130)
button=Button(struct,text="Search",font=("Times",10,"bold"),width=30,bd=2,command=search)
button.place(x=50,y=170)
struct.mainloop()