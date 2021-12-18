from tkinter import *

win = Tk()
win.title("radio button")
win.geometry("500x500")


def v_radio():
    pass


def click():
    pass


rb1 = Radiobutton(win, text="BCA", value=1, variable=v_radio)
rb2 = Radiobutton(win, text="MCA", value=2, variable=v_radio)
rb3 = Radiobutton(win, text="PGD", value=3, variable=v_radio)
btn1 = Button(win, text="submit", command=click)


def v_gender():
    pass


def click2():
    pass


g1 = Radiobutton(win, text="MALE", value=1, variable=v_gender)
g2 = Radiobutton(win, text="FEMALE", value=2, variable=v_gender)
btn2 = Button(win, text="submit", command=click2)

rb1.pack()
rb2.pack()
rb3.pack()
btn1.pack()
g1.pack()
g2.pack()
btn2.pack()

win.mainloop
