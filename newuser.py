import requests,webbrowser
import os
import os.path
import sys
import time
from bs4 import BeautifulSoup
from tkinter import *
import mysql.connector as mycon
con = mycon.connect(host='localhost', user='root', password = "1234")
cur = con.cursor()
cur.execute("create database if not exists wrs")
cur.execute("use wrs")
cur.execute("create table if not exists users(name varchar(20), pwd varchar(20))")
con.commit()
struct=Tk()
struct.geometry("450x350")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")
text=StringVar()
text1=StringVar()
yo=100
def geterror():
    label=Label(struct,text="USERNAME ALREADY EXISTS!\nRETRY!",bg="teal",fg="red",font=("Times",15,"bold"))
    label.place(x=70,y=yo+170)

   
def entry():
    username=(text.get())
    password=(text1.get())
    file_exists = os.path.exists(username+'.txt')
    cur.execute("select count(*) from users where name='"+username+"'")
    if (cur.fetchall()[0][0]==1):
        geterror()
    else:
        cur.execute("insert into users values('"+username+"','"+password+"')")
        con.commit()
        newuserfun()
def newuserfun():
    ''' labelp=Label(struct,text="New Account created!\nReturning to home screen!",bg="teal",fg="white",font=("Times",15,"bold"))
    labelp.place(x=90,y=yo+170)'''
    time.sleep(1)
    #struct.destroy()
    struct.destroy()
    os.system("py login.py 8")
    'here label not placing before os or time. so first new window, if closed, then label coming'
    
  
label=Label(struct,text="Enter New Username",bg="teal",fg="white",font=("Times",15,"bold"))
label.place(x=100,y=yo)

enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=100,y=yo+30)

label1=Label(struct,text="PASSWORD",bg="teal",fg="white",font=("Times",15,"bold"))
label1.place(x=100,y=yo+60)

enter1=Entry(struct,font=("Times",10,"bold"),textvar=text1,width=30,bd=2,bg="white")
enter1.place(x=100,y=yo+90)

button=Button(struct,text="Submit",font=("Times",10,"bold"),width=15,bd=2,command=entry)
button.place(x=150,y=yo+140)
    
struct.mainloop()

