from tkinter import *

win = Tk()
win.title("list box control")
win.geometry("500x500")

lb = Label(win, text="select any one language !", font=("", 10))
lb.pack()
clicked = StringVar()

main_menu = OptionMenu(win, clicked, "flutter", "c++", "c", "java", "python")
main_menu.pack()
win.mainloop()