from tkinter import *
root = Tk()

# Commands for button clicks
def Click_Nginamo():
    Text_Label = Label(root, text="Click ng inamo")
    Text_Label.pack()

def CLick_Submit():
    Hello_User = "Hello " + Form_Entry.get() + "!"
    Text_Label = Label(root, text=Hello_User)
    Text_Label.pack()              


# 1.1 Prompt for input
Name_Prompt = Label(root, text="Enter Your Name:")
Name_Prompt.pack()

# 1.2 Entry form
Form_Entry = Entry(root, width=50, borderwidth=4, bg="lightgray", fg="")
Form_Entry.pack()
Form_Entry.insert(0, "Default Text")

# 1.3 Submit button, command calls the function when button is clicked
Form_Entry_Button = Button(root, text="Submit My Name", command=CLick_Submit)
Form_Entry_Button.pack()

root.mainloop()

