import  tkinter as tk

win = tk.Tk()
win.title("pack")
win.geometry('200x200')
btn1 = tk.Button(win, text="button1")
btn2 = tk.Button(win, text="button2")

#btn1.pack()
#btn2.pack()

btn1.grid(column=1, row=1)
btn2.grid(column=2, row=2)

win.mainloop()


