#  create a label and change the label font style

from tkinter import *

root = Tk()

label1 = Label(root, text='This is label with styled font', font=('Times New Roman', 20, 'bold'))
label1.pack()  

root.mainloop()