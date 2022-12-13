from cProfile import label
from tkinter import *

root = Tk()

e = Entry(root,width=50, bg="#000000", fg="#FFFFFF")
#borderwidth=5
e.pack()
e.insert(0, "Enter Your Name: ")



def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name",padx=50,pady=50,command=myClick,fg="#ffffff",bg="red")
#state=DISABLED,padx=50,pady=50

myButton.pack()


root.mainloop()