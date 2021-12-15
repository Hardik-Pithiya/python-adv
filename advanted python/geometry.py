import tkinter as tk

win = tk.Tk()
win.title("first app")

txt =win.title()
print(txt)

win.geometry("500x500")
win.resizable(True,True)
win.minsize(100,100)
win.maxsize(600,600)
win.attributes('-alpha',1)
win.attributes('-topmost',0)

win.mainloop()