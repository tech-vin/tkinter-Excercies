from tkinter import *

root = Tk()
canvas_width = 100
canvas_height = 80

w = Canvas(root, width = canvas_width, height = canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#345")

root.mainloop()