from cProfile import label
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="I clicked a button, oh no")
    myLabel.pack()

myButton = Button(root, text="Click me!",padx=50,pady=50,command=myClick,fg="#ffffff",bg="red")
#state=DISABLED,padx=50,pady=50

myButton.pack()


root.mainloop()