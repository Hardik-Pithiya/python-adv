import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector

win = Tk()
win.geometry("800x500")
global e1
global e2
global e3
global e4

l1=tk.Label(win, text="Student Registation", fg="black", font=(None, 30))
lid = Label(win, text="Student Id")
lsnm = Label(win, text="Student Name")
lcour = Label(win, text="Cours")
lfees = Label(win, text="Fees")

l1.place(x=400, y=5)
lid.place(x=10, y=10)
lsnm.place(x=10, y=40)
lcour.place(x=10, y=70)
lfees.place(x=10, y=100)

e1 = Entry(win)
e2 = Entry(win)
e3 = Entry(win)
e4 = Entry(win)

e1.place(x=140, y=10)
e2.place(x=140, y=40)
e3.place(x=140, y=70)
e4.place(x=140, y=100)

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['stname'])
    e3.insert(0, select['course'])
    e4.insert(0, select['fee'])

def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fees = e4.get()

    mydb = mysql.connector.connect(host="localhost", user="root", password="", database='student')
    mycur=mydb.cursor()

    try:
        sql = "INSERT INTO stdinfo (id,stname,course,fee) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, fees)
        mycur.execute(sql, val)
        mydb.commit()
        lastid = mycur.lastrowid
        messagebox.showinfo("information", "Record inserted successful...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except EXCEPTION as e:
        print(e)
        mydb.rollback()
        mydb.close()

def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fees = e4.get()

    mydb = mysql.connector.connect(host="localhost", user="root", password="", database='student')
    mycur = mydb.cursor()

    try:
        sql = "Update stdinfo set stname = %s, course = %s, fee = %s, where id = %s"
        val = (studid, studname, coursename, fees)
        mycur.execute(sql, val)
        mydb.commit()
        lastid = mycur.lastrowid
        messagebox.showinfo("information", "Record Update successful...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except EXCEPTION as e:
        print(e)
        mydb.rollback()
        mydb.close()

def delete():
    studid = e1.get()

    mydb = mysql.connector.connect(host="localhost", user="root", password="", database='student')
    mycur = mydb.cursor()

    try:
        sql = "delete from stdinfo where id = %s"
        val = (studid)
        mycur.execute(sql, val)
        mydb.commit()
        lastid = mycur.lastrowid
        messagebox.showinfo("information", "Record Delete successful...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except EXCEPTION as e:
        print(e)
        mydb.rollback()
        mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database='student')
    mycur = mydb.cursor()
    mycur.execute("SELECT id, stname, course,fee from stdinfo")
    records = mycur.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mydb.close()

def search():
    pass


b1 = Button(win, text="Add", command=Add, height=3, width=13)
b2 = Button(win, text="Update", command=update, height=3, width=13)
b3 = Button(win, text="Delete", command=delete, height=3, width=13)
b4 = Button(win, text="search", command=search, height=3, width=13)
b5 = Button(win, text="close", command=win.destroy, height=3, width=13 )

b1.place(x=30, y=130)
b2.place(x=140, y=130)
b3.place(x=250, y=130)
b4.place(x=80, y=190)
b5.place(x=190, y=190)

cols = ("Id", "StuName", "course", "fees")
listBox = ttk.Treeview(win, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=250)

show()
listBox.bind('<Double-Button-1>', GetValue)

win.mainloop()