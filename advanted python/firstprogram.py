import tkinter as  tk
from tkinter import Button

win = tk.Tk()
#win.eval('tk:: PlaceWindow . center')
bt = tk.Button(win, text = "clik" , width=20,  height=2)
bt.place(x=50,y=50)

win.mainloop()