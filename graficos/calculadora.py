from  tkinter import *
raiz=Tk()
mi_frame=Frame(raiz)
mi_frame.pack()
operacion=""
resultado=0

# ----------------pantalla------------------------------
numeroPantalla=StringVar()

pantalla=Entry(mi_frame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg='black',fg="#03f943",justify="right")

# --------pulsaciones del teclado-------------
def numeroPulsado(num):
    global  operacion
    if operacion !="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
        # else:
        #     if operacion=="resta":
        #         numeroPantalla.set(numeroPantalla.get() - num)
        #     else:
        #         if operacion=="multiplicacion":
        #             numeroPantalla.set(numeroPantalla.get() * num)
        #         else:
        #             if operacion=="division":
        #                 numeroPantalla.set(numeroPantalla.get() / num)




#    --------funcion suma----------------------
def suma(num):
    global operacion
    global  resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)
# --------------funcion el_resultado---------------
def el_resultado():
    global resultado
    global operacion
    if operacion=="suma":
        numeroPantalla.set(resultado+ int(numeroPantalla.get()))
        resultado=0
    # if operacion=="resta":
    #     numeroPantalla.set(resultado - int(numeroPantalla.get()))
    #     resultado = 0


    # print(int(numeroPantalla))
def resta(num):
    global operacion
    global  resultado
    resultado=resultado-int(num)
    operacion="resta"
    numeroPantalla.set(resultado)
# -------------fila 1-------------------------------------

boton7=Button(mi_frame,text="7", width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(mi_frame,text="8", width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(mi_frame,text="9", width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
boton_div=Button(mi_frame,text="/", width=3)
boton_div.grid(row=2,column=4)

# -------------fila 2-------------------------------------

boton4=Button(mi_frame,text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(mi_frame,text="5", width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(mi_frame,text="6", width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
boton_mul=Button(mi_frame,text="x", width=3)
boton_mul.grid(row=3,column=4)


# -------------fila 3-------------------------------------

boton1=Button(mi_frame,text="1", width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(mi_frame,text="2", width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(mi_frame,text="3", width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
boton_resta=Button(mi_frame,text="-", width=3,command=lambda :resta(numeroPantalla.get()))
boton_resta.grid(row=4,column=4)

# -------------fila 4-------------------------------------

boton0=Button(mi_frame,text="0", width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
boton_coma=Button(mi_frame,text=",", width=3,command=lambda:numeroPulsado(","))
boton_coma.grid(row=5,column=2)
boton_sum=Button(mi_frame,text="+", width=3 , command=lambda :suma(numeroPantalla.get()))
boton_sum.grid(row=5,column=4)
boton_igual=Button(mi_frame,text="=", width=3, command=lambda :el_resultado())
boton_igual.grid(row=5,column=3)


raiz.mainloop()