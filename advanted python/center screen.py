from  tkinter import *

win = Tk()
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

positionRight = int(win.winfo_screenmmwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenmmheight()/2 - windowHeight/2)
win.geometry("+{}+{}".format(positionRight, positionDown))

win.mainloop()


