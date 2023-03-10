from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Adding Frames')
root.iconbitmap('D:/Programs/ry.ico')

# create 4 frames
frame1 = LabelFrame(root, text="Frame1:", padx=5, pady=5)
frame1.grid(row=0, column=0, padx=20, pady=20)

frame2 = LabelFrame(root, text="Frame2:", padx=5, pady=5)
frame2.grid(row=0, column=1, padx=20, pady=20)

frame3 = LabelFrame(root, text="Frame3:", padx=5, pady=5)
frame3.grid(row=1, column=0, padx=20, pady=20)

frame4 = LabelFrame(root, text="Frame4:", padx=5, pady=5)
frame4.grid(row=1, column=1, padx=20, pady=20)


# Create Items
item1 = Label(frame1, text="item 1")
item1.grid(row=0, column=0)

item2 = Label(frame2, text="item 2")
item2.grid(row=0, column=0)

item3 = Label(frame3, text="item 3")
item3.grid(row=0, column=0)

item4 = Label(frame4, text="item 4")
item4.grid(row=0, column=0)


#Create buttons
b1 = Button(frame1, text="B1")
b1.grid(row=0, column=1)

b2 = Button(frame2, text="B2")
b2.grid(row=0, column=1)

b3 = Button(frame3, text="B3")
b3.grid(row=0, column=1)

b4 = Button(frame4, text="B4")
b4.grid(row=0, column=1)


root.mainloop()