import  tkinter as tk
from  tkinter import messagebox

win =tk.Tk()
win.geometry("500x500")

def btn_click():
   #messagebox.showinfo(title= "first massagebox", message="Hello")
   # messagebox.showwarning(title="first massagebox", message="Hello")
   #messagebox.showerror(title="first massagebox", message="Hello")

    response = messagebox.askokcancel(title="confirmation", message="Delete")
    if response == True:
        messagebox.showinfo("title", "you can click ok")
    else:
        messagebox.showinfo("title", "you can click cancle")
btn = tk.Button(win, text="click", command = btn_click)


btn.pack()
win.mainloop()