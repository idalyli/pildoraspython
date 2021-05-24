from tkinter import *

root=Tk()
my_frame=Frame(root, width=500,height=400)
my_frame.pack()
my_label=Label(my_frame,text="Hola alumnos de python",fg="purple")
my_label.place(x=100,y=200)

root.mainloop()