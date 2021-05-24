import  sqlite3
mi_conexion=sqlite3.connect("GestionProductos")
mi_cursor=mi_conexion.cursor()
#
# mi_cursor.execute('''
# CREATE TABLE PRODUCTOS(
# ID INTEGER PRIMARY KEY  AUTOINCREMENT,
# NOMBRE_ARTICULO VARCHAR (50) UNIQUE,
# PRECIO INTEGER,
# SECCION VARCHAR (20)
# )
# ''')
#
# productos=[
#     ("pelota",20,"jugueteria"),
#     ("pantalo",15,"confeccion"),
#     ("destornillador",25,"ferrreteria"),
#     ("jarron",45,"ceramica")
# ]
# mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)


mi_cursor.execute("DELETE  FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pelota'")

mi_conexion.commit()
mi_conexion.close()