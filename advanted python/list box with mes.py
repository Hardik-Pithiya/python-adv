from tkinter import *

from tkinter import messagebox

win = Tk()
win.geometry("500x500")
win.title("list box 2")

lb = Listbox(win)
lb.insert(1, 'bca')
lb.insert(2, 'mca')
lb.insert(3, 'pgd-ca')
lb.insert(4, 'it')

lb.pack()


def btn_click():
    curbside = lb.curselection()
    for i in curbside:
        messagebox.showinfo("list box widget example", lb.get(curbside))


btn = Button(win, text="click", command=btn_click)
btn.pack()

win.mainloop()
