# create a Spinbox widget using tkinter module.

from tkinter import *
root = Tk()
txt_var = DoubleVar()
spin_box = Spinbox(root, from_= 0.6, to= 50.0, increment = 0.01,textvariable = txt_var)
spin_box.pack()


root.mainloop()
