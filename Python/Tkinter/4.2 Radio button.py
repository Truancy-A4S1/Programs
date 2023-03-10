from tkinter import *

root = Tk()
root.title('Adding Frames')
root.iconbitmap('D:/Programs/ry.ico')

# Codemy Example
# to be update when user chose a radio button
bariabol = IntVar() #StringVar(), FloatVar(), BooleanVar(), DoubleVar()
bariabol.set("2")

def radio_func(param):
    B_label = Label(root, text=param)
    B_label.pack()

B1 = Radiobutton(root, text="Bariabol = 1", variable=bariabol, value=1, command=lambda: radio_func(bariabol.get()))
B1.pack()

B2 = Radiobutton(root, text="Bariabol = 2", variable=bariabol, value=2, command=lambda: radio_func(bariabol.get()))
B2.pack()

B_label = Label(root, text="Enter a value")
B_label.pack()













root.mainloop()