from tkinter import *

#make a window
root = Tk()

# when the button is clicked
def myClick():
    myLabelClick = Label(root, text="CLICK CLICK CLICK ULOL")
    myLabelClick.grid(row=9,column=0)

entryForm = Entry(root, width=50, bg="lightblue", borderwidth=3)    #borderwidth is the depth
entryForm.grid(row=1,column=3)

# Creating myLabel widget
myLabel1 = Label(root, text="Hilu Wurld!")
myLabel2 = Label(root, text="This is awesome!")
# Shoving everything in the window
#myLabel.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Command is the finction that will be executed when the user clicked the button
myButton = Button(root, text="Button ng inamo", command=myClick, padx=10, pady=20)
blueButton = Button(root, text="white fg, black bg", fg="white", bg="black")

entryFormButton = Button(root, text=entryForm.get()) #get() get the value you input


myButton.grid(row=2,column=0)
blueButton.grid(row=2, column=1)

# Loop the window
root.mainloop()

