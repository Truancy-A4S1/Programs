from tkinter import *

root = Tk()

def add():
    pass

# Prompt
Prompt = Label(root, text="Calculator Yarn?")
Prompt.grid(row=0, column=0, columnspan=3)

# Text Box
T_box = Entry(root)
T_box.grid(row=1, column=0, columnspan=3)


button1 = Button(root, text="1", padx=20, pady=20)
button2 = Button(root, text="2", padx=20, pady=20)
button3 = Button(root, text="3", padx=20, pady=20)
button4 = Button(root, text="4", padx=20, pady=20)
button5 = Button(root, text="5", padx=20, pady=20)
button6 = Button(root, text="6", padx=20, pady=20)
button7 = Button(root, text="7", padx=20, pady=20)
button8 = Button(root, text="8", padx=20, pady=20)
button9 = Button(root, text="9", padx=20, pady=20)
button0 = Button(root, text="0", padx=20, pady=20)

buttonClear = Button(root, text="Clear", padx=45, pady=20)
buttonAdd = Button(root, text="+", padx=20, pady=20)
buttonSubtract = Button(root, text="-" , padx=55, pady=20)


button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=5, column=0)

buttonClear.grid(row=5, column=1, columnspan=2)
buttonAdd.grid(row=6, column=0)
buttonSubtract.grid(row=6, column=1, columnspan=2)

root.mainloop()