import sqlite3
mi_conexion=sqlite3.connect("PrimeraBase")
mi_cursor=mi_conexion.cursor()

# mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20)) ")
# mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# variosProductos=[
#     ("Camiseta",10,"Deportes"),
#     ("Jarron",90,"Ceramica"),
#     ("Camion",20,"Jugueteria")
# ]
# mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)

mi_cursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=mi_cursor.fetchall()
for producto in variosProductos:
    print("Nombre Articulo:", producto[0], "Seccion: ",producto[2])
mi_conexion.commit()
mi_conexion.close()