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
cur.execute("create table if not exists users(name varchar(20), pwd varchar(20))")
con.commit()
struct=Tk()
struct.geometry("500x330")
struct.title("WRS")
label=Label(struct,text="WEBSITE RANKING SYSTEM",bg="teal",fg="white",font=("Times",20,"bold"))
label.place(x=40,y=40)
struct.config(background="teal")
text=StringVar()
text1=StringVar()
err=1
yo=100
n = len(sys.argv)
if (n>1):
    struct.geometry("500x330")
    labelp=Label(struct,text="New Account created!\nLogin with new details!",bg="teal",fg="white",font=("Times",15,"bold"))
    labelp.place(x=100,y=250)
def geterror():
    labelq=Label(struct,text="USERNAME DOESN'T EXIST!\nRETRY!",bg="teal",fg="red",font=("Times",15,"bold"))
    labelq.place(x=70,y=yo+150)


def entry():
    username=(text.get())
    password=(text1.get())
    #file_exists = os.path.exists(username+'.txt')
    cur.execute("select count(*) from users where name='"+username+"'")
    if (cur.fetchall()[0][0]!=1):
    #check and input
        geterror()
    else:
        cur.execute("select pwd from users where name='"+username+"'")
        pwd=cur.fetchall()[0][0]
        if (pwd==password):
            struct.destroy()
            os.system("py home.py"+" "+username)
        else:
            label=Label(struct,text="PASSWORD MISMATCH!\nRETRY!",bg="teal",fg="red",font=("Times",17,"bold"))
            label.place(x=70,y=yo+150)
    #check for error

def newuserfun():
    struct.destroy()
    os.system("py newuser.py")
  
label=Label(struct,text="USERNAME",bg="teal",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)

enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=200,y=105)

label1=Label(struct,text="PASSWORD",bg="teal",fg="white",font=("Times",15,"bold"))
label1.place(x=50,y=130)

enter1=Entry(struct,font=("Times",10,"bold"),textvar=text1,width=30,bd=2,bg="white")
enter1.place(x=200,y=135)

button=Button(struct,text="Submit",font=("Times",10,"bold"),width=15,bd=2,command=entry)
button.place(x=150,y=180)

newuser=Button(struct,text="New User Register Here",font=("Times",10,"bold"),width=30,bd=2,command=newuserfun)
newuser.place(x=100,y=220)

struct.mainloop()