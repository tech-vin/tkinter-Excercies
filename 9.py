from tkinter import *
from tkinter import ttk

root = Tk()
str_var = StringVar()
my_combo = ttk.Combobox(root, textvariable = str_var, values = ['PHP', 'Python', "Java"])

my_combo.pack()
root.mainloop()