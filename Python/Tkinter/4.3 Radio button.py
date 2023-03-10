# Working with many radio buttons

from tkinter import *

root = Tk()
root.title('Radio Buttons using For Loop')
root.iconbitmap('D:/Programs/ry.ico')

# List of tuples
Pizza_Toppings = [
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Bacon","Bacon"),
    ("Onions","Onions"),
    ("Sausage","Sausage"),
    ("Pepperoni","Pepperoni"),
]

pizza = StringVar() #IntVar(), FloatVar(), BooleanVar(), DoubleVar()
pizza.set("Cheese")

for text, mode in Pizza_Toppings:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def radio_func(param):
    b_label = Label(root, text=param)
    b_label.pack()


b_label = Label(root, text="Enter a value")
b_label.pack()

b_button = Button(root, text="See More!", command=lambda: radio_func(pizza.get()))
b_button.pack()












root.mainloop()