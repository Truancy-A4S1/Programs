from tkinter import *
from tkinter import messagebox # message box interface
from PIL import ImageTk, Image # Image objects
from tkinter import filedialog # file dialog interface

root = Tk()
root.title('Original Window')
root.iconbitmap('D:/Programs/ry.ico')

root.filename = filedialog.askopenfile(initialdir="/Programs/Python/Image.res", 
                                       title="File Dialog ng Inamo", 
                                       filetypes=(
                                        (".PNG files", "*.png"),
                                        ("ALL files", "*.*")))
label = Label(root, text=root.filename.name)
label.pack()

image = ImageTk.PhotoImage(Image.open(root.filename.name))
img_label = Label(image=image).pack()

mainloop()