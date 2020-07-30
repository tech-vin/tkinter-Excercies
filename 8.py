from tkinter import *

root = Tk()

def print_message():
    return Label(root, text="Hello").pack()

Button(root, text= 'Message', command = print_message).pack()
Button(root, text = "exit", command = quit).pack()

root.mainloop()