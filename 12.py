# insert a string at the begining
# insert rest of the characters 
# remove first and last character


from tkinter import *

root = Tk()

txt = Text(root)
txt.insert('1.0', '- Python excercises, solution -')
txt.insert('1.19', ' practice, ')

txt.delete('1.0')
txt.delete('end -2 chars')
txt.pack()
root.mainloop()