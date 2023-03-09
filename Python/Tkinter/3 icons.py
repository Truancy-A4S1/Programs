from tkinter import *
# Install PIL by typing pip install Pillow in the terminal
from PIL import ImageTk, Image

root = Tk()
root.title('Icons and Images')
# Icon 
root.iconbitmap('D:/Programs/ry.ico')

my_img = ImageTk.PhotoImage(Image.open('D:/Programs/Python/Image.res/02.png').resize((400,400)))

my_label = Label(image=my_img, padx=40, pady=40)

my_label.pack()










# Exit button
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()