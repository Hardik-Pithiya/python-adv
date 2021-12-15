import tkinter as tk
from tkinter import StringVar, messagebox
import  studentcrud2 as sc

win = tk.Tk()
win.title("student crud")
win.geometry("500x500")
windgetFrame = tk.Frame(win)
windgetFrame.place(x=50, y=50)

v_rno = StringVar()
v_nm = StringVar()
v_city = StringVar()

lblrno = tk.Label(windgetFrame, text="Roll no")
lblnm = tk.Label(windgetFrame, text="Nmae")
lblcity = tk.Label(windgetFrame, text="city")

lblrno.grid(row=1, column=1)
lblnm.grid(row=2, column=1)
lblcity.grid(row=3, column=1)

entryrno = tk.Entry(windgetFrame, textvariable = v_rno)
entrynm = tk.Entry(windgetFrame, textvariable = v_nm)
entrycity = tk.Entry(windgetFrame, textvariable = v_city)

entryrno.grid(row=1, column=2)
entrynm.grid(row=2, column=2)
entrycity.grid(row=3, column=2)
def btn_insert():
    pass
def btn_update():
    pass
def btn_delete():
    pass

btninsert = tk.Button(windgetFrame, text="insert", command=btn_insert)
btnupdate = tk.Button(windgetFrame, text="update", command=btn_update)
btndelete = tk.Button(windgetFrame, text="delete", command=btn_delete)
btnclose = tk.Button(windgetFrame, text="close", command=win.destroy)

btninsert.grid(row=4, column=1)
btnupdate.place(x=41, y=63)
btndelete.place(x=88, y=63)
btnclose.place(x=130, y=63)



win.mainloop()