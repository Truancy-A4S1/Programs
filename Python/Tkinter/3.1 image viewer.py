from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons and Images')
root.iconbitmap('D:/Programs/ry.ico')

img1 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/01.png').resize((400,400)))
img2 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/02.png').resize((400,400)))
img3 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/03.png').resize((400,400)))
img4 = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/04.png').resize((400,400)))
image_list = [img1, img2, img3, img4]


my_label = Label(image=img1)
my_label.grid(row=1, column=0, columnspan=3)

def next_command(image_number):
    global my_label
    global button_prev
    global button_next

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_next = Button(root, text='>>', command=lambda: next_command(image_number+1))
    button_prev = Button(root, text='<<', command=lambda: prev_command(image_number-1))
    button_quit = Button(root, text="Exit", command=root.quit)

    if (len(image_list) == image_number):
        button_next = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)

    button_prev.grid(row=2, column=0)
    button_quit.grid(row=2, column=1)
    button_next.grid(row=2, column=2)


def prev_command(image_number):
    global my_label
    global button_prev
    global button_next

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_next = Button(root, text='>>', command=lambda: next_command(image_number+1))
    button_prev = Button(root, text='<<', command=lambda: prev_command(image_number-1))
    button_quit = Button(root, text="Exit", command=root.quit)
    
    if(image_number-1 == 0):
        button_prev = Button(root, text='<<', state=DISABLED)
    
    my_label.grid(row=1, column=0, columnspan=3)

    button_prev.grid(row=2, column=0)
    button_quit.grid(row=2, column=1)
    button_next.grid(row=2, column=2)



# Button definition
button_next = Button(root, text='>>', command=lambda: next_command(2))
button_quit = Button(root, text="Exit", command=root.quit)
button_prev = Button(root, text='<<', state=DISABLED)

# Button position
button_prev.grid(row=2, column=0)
button_quit.grid(row=2, column=1)
button_next.grid(row=2, column=2)

root.mainloop()