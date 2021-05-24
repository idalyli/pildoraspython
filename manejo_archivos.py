from  io import open
archivo_texto=open('archivo.txt',"r+")
# print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta es una nueva linea insertada\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()