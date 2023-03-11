from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Radio Buttons using For Loop')
root.iconbitmap('D:/Programs/ry.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup(box_type):
    if(box_type == "showinfo"):
        messagebox.showinfo("showinfo!", "Task failed successfully!")
    elif(box_type == "showwarning"):
        messagebox.showwarning("Error!", "Task failed successfully!")
    elif(box_type == "askquestion"):
        messagebox.askquestion("Error!", "Task failed successfully!")
    elif(box_type == "askokcancel"):
        messagebox.askokcancel("Error!", "Task failed successfully!")
    elif(box_type == "showerror"):
        messagebox.askokcancel("Error!", "Task failed successfully!")


Button(root, text='showinfo', command=lambda: popup('showinfo')).pack()
Button(root, text='showwarning', command=lambda: popup('showwarning')).pack()
Button(root, text='askquestion', command=lambda: popup('askquestion')).pack()
Button(root, text='askokcancel', command=lambda: popup('askokcancel')).pack()
Button(root, text='showerror', command=lambda: popup('showerror')).pack()


root.mainloop()