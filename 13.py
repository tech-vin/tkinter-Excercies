
# Create three single line text-box to accept a value from the user using tkinter module

from tkinter import *

root = Tk()

name_lbl = Label(root, text="Name")
name_lbl.place(x=30, y=30)
name_tf = Entry(root)
name_tf.place(x=80, y=30)

id_lbl = Label(root, text="UID")
id_lbl.place(x=30, y=60)
id_tf = Entry(root)
id_tf.place(x=80, y=60)

pwd_lbl = Label(root, text="Password")
pwd_lbl.place(x=30, y=90)
pwd_tf = Entry(root)
pwd_tf.place(x=80, y=90)
root.mainloop()