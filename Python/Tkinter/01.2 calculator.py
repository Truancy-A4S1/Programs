from tkinter import *

root = Tk()
root.title("Calcu ng Inamo")

def button_click(num):
    current = T_box.get()
    T_box.delete(0, END)
    T_box.insert(0, str(current) + str(num))
    
def button_clear():
    T_box.delete(0,END)

def button_add():
    global operation
    operation = '+'
    global fnum
    fnum = float(T_box.get())
    T_box.delete(0, END)

def button_sub():
    global operation
    operation = '-'
    global fnum
    fnum = float(T_box.get())
    T_box.delete(0, END)

def button_mul():
    global operation
    operation = '*'
    global fnum
    fnum = float(T_box.get())
    T_box.delete(0, END)

def button_div():
    global operation
    operation = '/'
    global fnum
    fnum = float(T_box.get())
    T_box.delete(0, END)

def button_dot():
    current = T_box.get()
    T_box.delete(0, END)
    T_box.insert(0, str(current) + ".")

def button_equal():
    global snum
    snum = float(T_box.get())
    T_box.delete(0, END)

    if(operation == '+'):
        T_box.insert(0, fnum + snum)
    elif(operation == '-'):
        T_box.insert(0, fnum - snum)
    elif(operation == '*'):
        T_box.insert(0, fnum * snum)
    elif(operation == '/'):
        T_box.insert(0, fnum / snum)
    else:
        T_box.insert(0, "Invalid Operation")


# Prompt
Prompt = Label(root, text="Python x Tkinter")
Prompt.grid(row=0, column=0, columnspan=3)

# Text Box
T_box = Entry(root, width=45, borderwidth=5)
T_box.grid(row=1, column=0, columnspan=3)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonSub = Button(root, text="-", padx=40, pady=20, command=button_sub)
buttonMul = Button(root, text="*", padx=40, pady=20, command=button_mul)
buttonDiv = Button(root, text="/", padx=40, pady=20, command=button_div)

buttonClear = Button(root, text="⌫", padx=83, pady=20, command=button_clear)
buttonEqual = Button(root, text="=" , padx=40, pady=20, command=button_equal)
buttonDot = Button(root, text=".", padx=44, pady=20, command=button_dot)

# Button Position in grid
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
buttonSub.grid(row=5, column=1)
buttonDiv.grid(row=5, column=2)

buttonAdd.grid(row=6, column=0)
buttonMul.grid(row=6, column=1)
buttonEqual.grid(row=6, column=2)

buttonClear.grid(row=7, column=0, columnspan=2)
buttonDot.grid(row=7, column=2)

root.mainloop()