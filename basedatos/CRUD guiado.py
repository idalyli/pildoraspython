import sqlite3
from  tkinter import *
from tkinter import messagebox

# ---------------------funciones-------------------------
def conexion_BBDD():
    my_conexion=sqlite3.connect("Usuarios")
    my_cursor=my_conexion.cursor()
    try:
        my_cursor.execute('''
        CREATE TABLE DATOSUSUARIOS(
        ID INTEGER  PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR (50),
        PASSWORD VARCHAR (50),
        LAST_NAME VARCHAR (10),
        ADDRESS VARCHAR (50),
        COMMENT VARCHAR (100))
        ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion!","La BBDD ya existe")

def exit_app():
    valor=messagebox.askquestion("Salir","Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
def cleaner():
    my_ID.set("")
    my_name.set("")
    my_password.set("")
    my_lastname.set("")
    my_address.set("")
    text_comment.delete(1.0,END)

def create():
    my_connect=sqlite3.connect("Usuarios")

    my_cursor=my_connect.cursor()

    # my_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES( NULL ,'" + my_name.get() +
    # "' ,'" + my_password.get() +
    # "','" + my_lastname.get() +
    # "','" + my_address.get() +
    # "','" + text_comment.get(1.0, END) + "')")

    datos=my_name.get(),my_password.get(),my_lastname.get(),my_address.get(),text_comment.get(1.0, END)

    my_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    my_connect.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")


def read():
    my_connect = sqlite3.connect("Usuarios")

    my_cursor = my_connect.cursor()
    my_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+my_ID.get())
    el_usuario=my_cursor.fetchall()
    for usuario in el_usuario:
        my_ID.set(usuario[0])
        my_name.set(usuario[1])
        my_password.set(usuario[2])
        my_lastname.set(usuario[3])
        my_address.set(usuario[4])
        text_comment.insert(1.0,usuario[5])
    my_connect.commit()

def update():
    my_connect = sqlite3.connect("Usuarios")

    my_cursor = my_connect.cursor()
    #
    # my_cursor.execute("UPDATE  DATOSUSUARIOS SET USER_NAME='" + my_name.get() +
    # "',PASSWORD='" + my_password.get() +
    # "',LAST_NAME='" + my_lastname.get() +
    # "',ADDRESS='" + my_address.get() +
    # "',COMMENT='" + text_comment.get("1.0",END) +
    # "' WHERE ID="+my_ID.get())
    datos = my_name.get(), my_password.get(), my_lastname.get(), my_address.get(), text_comment.get(1.0, END)

    my_cursor.execute("UPDATE DATOSUSUARIOS  SET USER_NAME=?, PASSWORD=?, LAST_NAME=?,ADDRESS=?,COMMENT=?" +
                      "WHERE ID="+my_ID.get(), (datos))


    my_connect.commit()

    messagebox.showinfo("BBDDD","Registro actualizado con exito")


def delete():
    my_connect=sqlite3.connect("Usuarios")

    my_cursor=my_connect.cursor()

    my_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+my_ID.get())

    my_connect.commit()
    messagebox.showinfo("BBDD","Registro eliminado con exito")


# -------------------------raiz----------------------------
root=Tk()
barra_menu=Menu(root)
root.config(menu=barra_menu,width=300,height=300)

# ------------------------menu BBDD--------------------------
bbdd_menu=Menu(barra_menu,tearoff=0)
bbdd_menu.add_command(label="Connect" ,command=conexion_BBDD)


bbdd_menu.add_command(label="Exit", command=exit_app)

# -----------------------------menu delete--------------------

delete_menu=Menu(barra_menu, tearoff=0)
delete_menu.add_command(label="Clean",command=cleaner)

# -----------------------------menu CRUD--------------------

CRUD_menu=Menu(barra_menu, tearoff=0)
CRUD_menu.add_command(label="Create", command=create)
CRUD_menu.add_command(label="Read",command=read)
CRUD_menu.add_command(label="Update", command=update)
CRUD_menu.add_command(label="Delete",command=delete)


# -----------------------------menu Help--------------------------------

help_menu=Menu(barra_menu, tearoff=0)
help_menu.add_command(label="License")
help_menu.add_command(label="About to")

#----------------asociar a la barra de menu los submenus------------------

barra_menu.add_cascade(label="BBDD",menu=bbdd_menu)
barra_menu.add_cascade(label="Clean",menu=delete_menu)
barra_menu.add_cascade(label="CRUD",menu=CRUD_menu)
barra_menu.add_cascade(label="Help",menu=help_menu)

# ---------------comienzo de campos----------------------------
my_frame=Frame(root)
my_frame.pack()

my_ID=StringVar()
my_name=StringVar()
my_lastname=StringVar()
my_password=StringVar()
my_address=StringVar()


cuadro_ID=Entry(my_frame,textvariable=my_ID)
cuadro_ID.grid(row=0,column=1, padx=10,pady=10)


cuadro_name=Entry(my_frame,textvariable=my_name)
cuadro_name.grid(row=1,column=1, padx=10,pady=10)
cuadro_name.config(fg="red",justify="right")

cuadro_password=Entry(my_frame,textvariable=my_password)
cuadro_password.grid(row=2,column=1, padx=10,pady=10)
cuadro_password.config(show="*")

cuadro_lastname=Entry(my_frame,textvariable=my_lastname)
cuadro_lastname.grid(row=3,column=1, padx=10,pady=10)

cuadro_address=Entry(my_frame,textvariable=my_address)
cuadro_address.grid(row=4,column=1, padx=10,pady=10)

text_comment=Text(my_frame,width=15, height=5)
text_comment.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(my_frame,command=text_comment.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")
text_comment.config(yscrollcommand=scrollVert.set)
# ---------------label-----------------
id_label=Label(my_frame,text="Id:")
id_label.grid(row=0,column=0,sticky="e",padx=10,pady=10)

name_label=Label(my_frame,text="Name:")
name_label.grid(row=1,column=0,sticky="e",padx=10,pady=10)

password_label=Label(my_frame,text="Password:")
password_label.grid(row=2,column=0,sticky="e",padx=10,pady=10)

lastname_label=Label(my_frame,text="Last Name:")
lastname_label.grid(row=3,column=0,sticky="e",padx=10,pady=10)

address_label=Label(my_frame,text="Address:")
address_label.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comment_label=Label(my_frame,text="Comment:")
comment_label.grid(row=5,column=0,sticky="e",padx=10,pady=10)

# ----------------botones-------------------
my_frame_buttons=Frame()
my_frame_buttons.pack()

button_create=Button(my_frame_buttons,text="Create",command=create)
button_create.grid(row=1,column=0,sticky="e", padx=10,pady=10)

button_read=Button(my_frame_buttons,text="Read",command=read)
button_read.grid(row=1,column=1,sticky="e", padx=10,pady=10)

button_update=Button(my_frame_buttons,text="Update",command=update)
button_update.grid(row=1,column=2,sticky="e", padx=10,pady=10)

button_delete=Button(my_frame_buttons,text="Delete",command=delete)
button_delete.grid(row=1,column=3,sticky="e", padx=10,pady=10)

root.mainloop()
