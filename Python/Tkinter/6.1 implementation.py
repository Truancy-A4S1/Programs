from tkinter import *
from tkinter import messagebox # message box interface
from PIL import ImageTk, Image # image objects
from tkinter import filedialog # file dialog interface
from tkinter.font import Font # font
from pathlib import Path # path objects

root = Tk()
root.title("Day 06 Implementation")
#root.iconbitmap("ry.ico")

# Set up font
MonoFont = Font( family="Courier", size=15, weight="normal", slant="roman", underline=0 )

# Frames
frame_calcu = LabelFrame(root, text="Calculator", pady=5, padx=5)
frame_calcu.grid(row=0, column=0, pady=10, padx=10)

frame_quiz = LabelFrame(root, text="Quiz", pady=5, padx=5)
frame_quiz.grid(row=0, column=1, pady=10, padx=10)

frame_image = LabelFrame(root, text="Image Viewer", pady=5, padx=5)
frame_image.grid(row=1, column=0, pady=10, padx=10)

                    # Calculator
# Function
def calculate(val):
    current = text_box.get()
    text_box.delete(0, END)
    text_box.insert(0, str(current) + str(val))

def operation(oper):
    global first_num
    global do_this

    do_this = oper
    first_num = float(text_box.get())
    text_box.delete(0, END)
    

def equal():
    global second_num
    second_num = float(text_box.get())
    text_box.delete(0, END)

    if (do_this == '+'):
        text_box.insert(0, first_num + second_num)
    elif (do_this == '-'):
        text_box.insert(0, first_num - second_num)
    elif (do_this == '*'):
        text_box.insert(0, first_num * second_num)
    elif (do_this == '/'):
        text_box.insert(0, first_num / second_num)

def clear():
    text_box.delete(0, END)

# Text Box
text_box = Entry(frame_calcu, width=20, borderwidth=4, font=MonoFont)
text_box.grid(row=0, column=0, columnspan=4)

# Button declaration
b0 = Button(frame_calcu, text="0", font=MonoFont, padx=20, pady=20, command = lambda: calculate(0))

b1 = Button(frame_calcu, text="1", font=MonoFont, padx=20, pady=20, command = lambda: calculate(1))
b2 = Button(frame_calcu, text="2", font=MonoFont, padx=20, pady=20, command = lambda: calculate(2))
b3 = Button(frame_calcu, text="3", font=MonoFont, padx=20, pady=20, command = lambda: calculate(3))

b4 = Button(frame_calcu, text="4", font=MonoFont, padx=20, pady=20, command = lambda: calculate(4))
b5 = Button(frame_calcu, text="5", font=MonoFont, padx=20, pady=20, command = lambda: calculate(5))
b6 = Button(frame_calcu, text="6", font=MonoFont, padx=20, pady=20, command = lambda: calculate(6))

b7 = Button(frame_calcu, text="7", font=MonoFont, padx=20, pady=20, command = lambda: calculate(7))
b8 = Button(frame_calcu, text="8", font=MonoFont, padx=20, pady=20, command = lambda: calculate(8))
b9 = Button(frame_calcu, text="9", font=MonoFont, padx=20, pady=20, command = lambda: calculate(9))

bAdd = Button(frame_calcu, text="+", font=MonoFont, padx=20, pady=20, command = lambda: operation("+"))
bSub = Button(frame_calcu, text="-", font=MonoFont, padx=20, pady=20, command = lambda: operation("-"))
bMul = Button(frame_calcu, text="*", font=MonoFont, padx=20, pady=20, command = lambda: operation("*"))
bDiv = Button(frame_calcu, text="/", font=MonoFont, padx=20, pady=20, command = lambda: operation("/"))

bEqual = Button(frame_calcu, text="=", font=MonoFont, padx=20, pady=20, command = equal)
bClear = Button(frame_calcu, text="⌫", font=MonoFont, padx=13, pady=20, command= clear)

# Button Position on grid
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
bDiv.grid(row=1,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bMul.grid(row=2,column=3)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
bSub.grid(row=3,column=3)

b0.grid(row=4,column=0)
bAdd.grid(row=4,column=1)
bEqual.grid(row=4,column=2)
bClear.grid(row=4,column=3)


# Image Viewer
viewer_win_caption = Label(frame_image, text="coming soon..")
viewer_win_caption.pack()
# TDL: choose a path -> get the files in that direcory -> create an image objects directed at each image path
# img_path = Path("D:\Programs\Python\Image.res")
# Make a LIST of .png files
# for filenames_from_file in img_path.glob("*.png"):
#    print(filenames_from_file)

# Image objects added to the list
img1 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/01.png').resize((265,265)))
img2 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/02.png').resize((265,265)))
img3 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/03.png').resize((265,265)))
img4 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/04.png').resize((265,265)))
image_list = [img1, img2, img3, img4]

# initial image 
img_label = Label(viewer_win_caption, image=img1)
img_label.grid(row=1, column=0, columnspan=3)

#functions
def img_next(img_num):
    global img_label
    global bNext
    global bPrev
    global bExit

    img_label.grid_forget()
    img_label = Label(viewer_win_caption, image=image_list[img_num])
    
    img_label.grid(row=1, column=0, columnspan=3)

    # Buttons (Prev is disabled because the first image is already being displayed)
    bNext = Button(viewer_win_caption, font=MonoFont, text="Next", command=lambda: img_next(img_num+1))
    bExit = Button(viewer_win_caption, font=MonoFont, text="Exit", command=root.quit)
    bPrev = Button(viewer_win_caption, font=MonoFont, text="Prev", command=lambda: img_prev(img_num-1))

    if(len(image_list) == img_num+1):
        bNext = Button(viewer_win_caption, font=MonoFont, text="Next", state=DISABLED)

    # Button positions
    bPrev.grid(row=2, column=0, padx=10, pady=5)
    bExit.grid(row=2, column=1, padx=10, pady=5)
    bNext.grid(row=2, column=2, padx=10, pady=5)

def img_prev(img_num):
    global img_label
    global bNext
    global bPrev
    global bExit

    img_label.grid_forget()
    img_label = Label(viewer_win_caption, image=image_list[img_num])
    img_label.grid(row=1, column=0, columnspan=3)

    # Buttons (Prev is disabled because the first image is already being displayed)
    bNext = Button(viewer_win_caption, font=MonoFont, text="Next", command=lambda: img_next(img_num+1))
    bExit = Button(viewer_win_caption, font=MonoFont, text="Exit", command=root.quit)
    bPrev = Button(viewer_win_caption, font=MonoFont, text="Prev", command=lambda: img_prev(img_num-1))

    if(img_num == 0):
        bPrev = Button(viewer_win_caption, font=MonoFont, text="Prev", state=DISABLED)

    # Button positions
    bPrev.grid(row=2, column=0, padx=10, pady=5)
    bExit.grid(row=2, column=1, padx=10, pady=5)
    bNext.grid(row=2, column=2, padx=10, pady=5)


# Buttons (Prev is disabled because the first image is already being displayed)
bNext = Button(viewer_win_caption, font=MonoFont, text="Next", command=lambda: img_next(2))
bExit = Button(viewer_win_caption, font=MonoFont, text="Exit", command=root.quit)
bPrev = Button(viewer_win_caption, font=MonoFont, text="Prev", state=DISABLED)

# Button positions
bPrev.grid(row=2, column=0, padx=10, pady=5)
bExit.grid(row=2, column=1, padx=10, pady=5)
bNext.grid(row=2, column=2, padx=10, pady=5)


# Quiz
Label(frame_quiz, text="coming soon..").pack()



# Calculator
# Image Viewer
# Frames
# Radio Button (Quiz)
# File Dialog

mainloop()