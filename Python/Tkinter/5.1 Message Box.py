from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Radio Buttons using For Loop')
root.iconbitmap('D:/Programs/ry.ico')

#askokcancel(return 1,0) askquestion(return yes, no) , showerror(return ok), showwarning(return ok), showinfo(return ok)

def popup():
    response = messagebox.askyesno("Do you like this?", "Choose a button below") # return boolean
    # Label(root, text = response).pack() # Get the value on messagebox

    if (response == True):
        Label(root, text ="I'm glad you liked it").pack()
    else:
        Label(root, text ="Bubu ka eh!").pack()
        

button1 = Button(root, text="Show PopUp", command=popup)
button1.pack()

root.mainloop()