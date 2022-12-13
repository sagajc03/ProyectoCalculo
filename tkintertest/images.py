from cProfile import label
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Something that happend to happens")
root.iconphoto(False,PhotoImage(file=r'ProyectoCalculo\tkintertest\ico\77115862_p0.png'))
#r (to produce a raw string)

my_img = ImageTk.PhotoImage(Image.open(r'ProyectoCalculo\tkintertest\ico\unknown.png'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program",command=root.quit)
button_quit.pack()

root.mainloop()