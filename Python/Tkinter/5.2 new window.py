from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Original Window')
root.iconbitmap('D:/Programs/ry.ico')

def openWin2():
    global img1 #global image
    top = Toplevel() #create a new window

    # window 2 title and logo
    top.title('Second Window')
    top.iconbitmap('D:/Programs/ry.ico')

    # image on window 2
    img1 = ImageTk.PhotoImage(Image.open("D:/Programs/Python/Image.res/01.png"))
    lbl1 = Label(top, image=img1).pack()

    # exit button
    btn = Button(top, text="Exit Win2", command=top.destroy)
    btn.pack()


button = Button(root, text="Open Win2", command=openWin2).pack()


mainloop()