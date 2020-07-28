# create title to widjet and label
from tkinter import *

root = Tk()
root.title('This is the title of the window')

label = Label(root, text="Representing Label")
label.pack()

root.mainloop()