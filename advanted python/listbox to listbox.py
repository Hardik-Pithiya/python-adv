from select import select
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x500")
win.title("listbox to listbox")

lb1 = Listbox(win)
lb1.insert(1, "BCA")
lb1.insert(2, "python")
lb1.insert(3, "java")
lb1.insert(4, "android")
lb1.insert(5, "flutter")

lb2 = Listbox(win)

lb1.place(x=50, y=100)
lb2.place(x=255, y=100)


def bt1():
    varlist = lb1.curselection()
    if varlist:
        var = varlist[0]
        val = lb1.get(var)
        lb1.delete(var)
        lb2.insert(END, val)



def bt2():
        varlist = lb1.select_set(0, END)
        if varlist:
            var = varlist[0, END]
            val = lb1.get(var)
            lb1.delete(var)
            lb2.insert(0, val)


def bt3():
    varlist = lb2.curselection()
    if varlist:
        var = varlist[0]
        val = lb2.get(var)
        lb2.delete(var)
        lb1.insert(END, val)


def bt4():
    varlist = lb2.select_set(0, END)
    if varlist:
        var = varlist[0, END]
        val = lb2.get(var)
        lb2.delete(var)
        lb1.insert(0, val)


def bt5():
    varlist = lb1.curselection()
    if varlist:
        var = varlist[0]
        val = lb1.get(var)
        lb1.delete(var)

def bt6():
    varlist = lb2.curselection()
    if varlist:
        var = varlist[0]
        val = lb2.get(var)
        lb2.delete(var)


btn1 = Button(win, text=">", command=bt1, width=10, height=2)
btn2 = Button(win, text=">>", command=bt2, width=10, height=2)
btn3 = Button(win, text="<", command=bt3, width=10, height=2)
btn4 = Button(win, text="<<", command=bt4, width=10, height=2)
btn5 = Button(win, text="Remove", command=bt5, width=10, height=2)
btn6 = Button(win, text="Remove", command=bt6, width=10, height=2)

btn1.place(x=175, y=100)
btn2.place(x=175, y=140)
btn3.place(x=175, y=180)
btn4.place(x=175, y=220)
btn5.place(x=70, y=265)
btn6.place(x=270, y=265)

win.mainloop()
