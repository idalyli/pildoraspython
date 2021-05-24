from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba")
# raiz.resizable(True,0)
# raiz.iconbitmap('libelula.ico')
# raiz.geometry("650x350")
raiz.config(bg="purple")

mi_frame=Frame()
mi_frame.pack()
mi_frame.pack(side="right", anchor="s")
mi_frame.config(width="650", height="350")
mi_frame.config(bg="pink")


raiz.mainloop()