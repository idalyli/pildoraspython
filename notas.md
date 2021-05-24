
###impresion en consola
print("hola')

### insertar comentario
   // #aqui un comentario
   
# tipos de datos

## numericos

enteros (int)

coma flotante(float)

complejos

## Textos
Pueden ir entre comillas  dobles"" o  simples '' o triple comilla """"""
esta ultima se utiliza cuando se requieren saltos de linea
ejm 
mensaje="""esto es un mensaje 
con tres saltos
de linea """

## Booleanos
 True
 False
 
# Operadores

##Aritmeticos 
Suma +, Resta -,Multiplicacion *, 
Division /,Modulo %,Divison entera // ,Exponente **
## Comparacion
igual que ==, mayor que >, diferente !=, menor que <
mayor o igual que >=, menor o igual que <=

#Logicos
AND, OR, NOT

# Asignacion
igual =, decremento -=, incremento +=, *=, /=, %=, **=, //=

# Especiales
IS, IS NOT, IN, NOT IN

# Variable

nombre
nombre_completo
en python todo 100% es un objeto
numero=5
type(numero)
<class 'int'>

# Condicional if

if number1 > number2:
    print('Yes')
        

if number1 > number2:
    print('Yes')
else:
    print('Not')

# Funciones
### predifinidas
las proporciona el lenguaje

### propias

declarar la funcion

def nombre_funcion():
    instrucciones de la funcion
    return(opcional)


def nombre_funcion(parametros):
    instrucciones de la funcion
    return(opcional)


llamar o invocar la funcion
nombre_funcion()
ejm:
def sum_number(number1, number2):
    return number2+number1


 print(sum_number(5, 6))
 
# listas

nombre_lista=[elem1,elem2,elem3...]
my_list = ['maria', 'jose', 'eli', 'agu']
print(my_list)

indice=posicion del elemento dentro de la lista
print(my_list[2])

cuando se introduce un indice negativo empieza a recorrer la lista desde el ultimo
elemento siendo este -1, el que sigue -2 y asi sucesivamente

## para acceder a una porcion de lista

print(my_list[0:3])-> acceder a los tres primeros elementos, incluyendo el que esta en el indice 0 y excluyendo el que esta
en el indice 3
print(my_list[:3])-> acceder a los tres primeros elementos
print(my_list[:])-> imprimir toda la lista
print(my_list[2:])-> si se prescinde del ultimo indice, tomara los dos ultimos elementos de la lista

my_list.append('Sandra')->adiciona un elemento a la lista, agregandolo al final de la lista
my_list.insert(2,'Sandra')-> inserta un elemento a la lista en la posicion 2, el primer parametro hacer refencia al indice y el segundo al valor
my_list.extend(['julian', 'pedro'])-> anadir mas de un elemento a una lista

## devolver el indice de un elemento en una lista

print(my_list.index('el valor'))

saber si un elemento se encuentra en una lista

print('juan' in my_list)-> devuelve True or False segun sea el caso

## eliminar un elemento de la lista

my_list.remove('eli')->elimina de la lista el elemento especificado

my_list.pop()-> elimina el ultimo elemento de la lista

## concatenar listas

    my_list = ['maria', 'jose', 'eli', 'agu']

    my_list2 = [1, 2]

    print(my_list2 + my_list)->[1, 2, 'maria', 'jose', 'eli', 'agu']

## operador * en lista es un repetidor

my_list = ['maria', 'jose', 'eli', 'agu']*2
print(my_list)->['maria', 'jose', 'eli', 'agu', 'maria', 'jose', 'eli', 'agu']

# Tuplas ->
listas inmutables, no se puede ni adicionar,quitar ,ni mover elementos, no permite busquedas (no indice) 
aunque en las ultimas version de python si lo permite si permite extraer porciones, el resultado de la extraccion es una nueva tupla
si permite comprobar que un elemento se encuentre o no en una tupla

nombre_tupla=(elem1,elem2,elem3...)

my_tupla = 'maria', 'jose', 'eli', 'agu'
print(my_tupla[1])->encontrar un elemento especifico por su indice
print('juan' in my_tupla)-> saber si un elemento se encuentra en una tupla

## convertir una tupla en lista

    my_tupla = 'maria', 'jose', 'eli', 'agu'
    my_list=list(my_tupla)
    
    print(my_list)->['maria', 'jose', 'eli', 'agu']

## convertir una lista en tupla

    my_list = ['maria', 'jose', 'eli', 'agu']
    my_tupla=tuple(my_list)
    print(my_tupla)->('maria', 'jose', 'eli', 'agu')

## como saber si un elemento en una tupla y cuantas veces

    my_list = ['maria', 'jose', 'eli', 'agu', 'eli']

    my_tupla = tuple(my_list)
    print('eli' in my_tupla)
    print(my_tupla.count('eli'))

## como saber la longitud de una tupla
    my_tupla = ('maria', 'jose', 'eli', 'agu', 'eli')
    print(len(my_tupla))

## definir tuplas unitarias
    my_tupla = ('maria', )

## empaquetado de tupla(definir la tupla sin parentesis)

    my_tupla = 'maria', 'jose', 'eli', 'agu'
## desempaquetado de tupla

    my_tupla = ('maria', 13, 1, 1995)
    name,day, mouth, year = my_tupla
    print(name,year,mouth,day)->maria 1995 1 13
# diccionarios

## definir un diccinario clave:valor

    my_dict = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres"}

## acceder a un elemento del diccionario

    nombre_dict[clave]

    print(my_dict["Francia"])
## agregar elementos a un diccionario

    print(sum_number(5, 6))
    my_dict = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres"}
    my_dict["Italia"] ="Lisboa"
    print(my_dict)->{'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Italia': 'Lisboa'}

## modificar el valor de un elemento de un diccionario

    my_dict = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres"}
    my_dict["Italia"] ="Lisboa"
    print(my_dict)->{'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Italia': 'Lisboa'}
    my_dict["Italia"]= "Roma"
    print(my_dict)->{'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Italia': 'Roma'}

## eliminar elementos de un  diccionario
    del my_dict["clave"]
    del my_dict["Reino Unido"]
## utilizar una tupla es para poner los valores para cada clave en un diccionario

    my_tuple = ('Alemania', "Francia", "Reino unido")
    my_dict = {my_tuple[0]: "Berlin", my_tuple[1]: "Paris", my_tuple[2]: "Londres"}
    print(my_dict)->{'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino unido': 'Londres'}
## tuplas con diversos tipos de datos
    my_dict = {23: "Jordan", "name": "Michael", "Team":" Chicago", "rings": [1991, 1992, 1997, 1998]}
    print(my_dict)
    print(my_dict["rings"])

    diccionario dentro de un diccionario

    my_dict = {23: "Jordan", "name": "Michael", "Team":" Chicago", "rings": {"temporadas":[1991, 1992, 1997, 1998]}}
    print(my_dict)->{23: 'Jordan', 'name': 'Michael', 'Team': ' Chicago', 'rings': {'temporadas': [1991, 1992, 1997, 1998]}}
    print(my_dict["rings"])->{'temporadas': [1991, 1992, 1997, 1998]}

## metodos con diccionarios

    my_dict = {23: "Jordan", "name": "Michael", "Team":" Chicago", "rings": {"temporadas":[1991, 1992, 1997, 1998]}}
    print(my_dict.keys())->dict_keys([23, 'name', 'Team', 'rings'])
    print(my_dict.values())->dict_values(['Jordan', 'Michael', ' Chicago', {'temporadas': [1991, 1992, 1997, 1998]}])
    print(len(my_dict))->4

# condicionales

    def evaluation(nota):
        valoracion="aprobado"
        if nota < 5:
            valoracion='suspenso'
        return valoracion

    print(evaluation(2))->suspenso

## else 
    
    print("verificacion de acceso")
    
    age_user = int(input('Cual es tu edad?'))
    
    
    def access(age_user):
        if age_user > 18:
            print('puede acceder')
        else:
            print('no tiene acceso permitido')
## elif
    print("verificacion de acceso")
    
    age_user = int(input('Cual es tu edad?'))
    
    
    def access(age_user):
        if age_user > 18 and age_user <= 100:
            print('puede acceder')
        elif age_user > 100:
            print("edad incorrecta")
        else:
            print('no tiene acceso permitido')




    print("verificacion de notas")

    nota_alumno = int(input('Cual es tu nota?'))
    
    
    def access(nota_alumno):
        if nota_alumno < 5:
            print('insuficiente')
        elif nota_alumno < 6:
             print('suficiente')
        elif nota_alumno < 7:
             print('Bien')
        elif nota_alumno < 9:
             print('notable')
        else:
             print('sobresaliente')

# Uso de concatenacion en condicionales
    
    def comparacion_salarios():
        salario_presidente = int(input("Introduce salario presidente"))
        print("salario presidente es:"+ str(salario_presidente))
        salario_director = int(input("Introduce salario director"))
        print("salario director es:"+ str(salario_director))
        salario_jefe_area = int(input("Introduce salario jefe de area"))
        print("salario jefe de area es:"+ str(salario_jefe_area))
        salario_administrativo = int(input("Introduce salario administrativo"))
        print("salario administrativo es:"+ str(salario_jefe_area))
        if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
            print("todo funciona")
        else:
            print("algo no funciona")


    comparacion_salarios()
## operador and
    def becas():
        print("Programa de becas")
        distancia_escuela = int(input("introduce la distacia a la escuela en km"))
        print(distancia_escuela)
        numero_hermanos = int(input("introduce numero hermanos"))
        print(numero_hermanos)
        salario_familiar = int(input("introduce salario anual bruto"))
        print(salario_familiar)
        if distancia_escuela > 40 and numero_hermanos >= 2 and salario_familiar <= 20000:
            print("Beca aprobada")
        else:
            print("Beca no fue aprobada")
## operador or
    def becas():
        print("Programa de becas")
        distancia_escuela = int(input("introduce la distacia a la escuela en km"))
        print(distancia_escuela)
        numero_hermanos = int(input("introduce numero hermanos"))
        print(numero_hermanos)
        salario_familiar = int(input("introduce salario anual bruto"))
        print(salario_familiar)
        if distancia_escuela > 40 and numero_hermanos >= 2 or salario_familiar <= 20000:
            print("Beca aprobada")
        else:
            print("Beca no fue aprobada")
## operador in

    def asignatura():
        print("Asignaturas optativas")
        print("Informatica grafica - Pruebas de sofware - Usabilidad y accesibilidad")
        opcion = input("Escriba una asignatura")
        asignatura_elegida = opcion.lower()
        if asignatura_elegida in ("informatica grafica","pruebas de software", "usabilidad y accesibilidad"):
            print("asginatura elegida" + asignatura_elegida)
        else:
            print("La asignatura escogida no esta contemplada")
# Bucle

    for variable in elemento a recorrer:
        cuerpo del bucle

    def print_msg():
        for i in [1, 2, 3, 4]:
            print("hola")

    ejmp 2:
    def print_msg():
        for i in ["primavera", "verano", "otono", "invierno"]:
            print(i)
    ejmp 3:
    def print_msg():
        for i in ["primavera", "verano", "otono", 3]:
            print("Hola",end=" ")
    print_msg()->Hola Hola Hola Hola 

    ejem 4: recorrer un string

    for i in "juan":
        print(i)

    ejem 5: cuando se usa range , se crea una especie de array de x elementos 
    for i in range(5):
        print(i)


# while
    i=1
    while i<=10:
        print("ejecucion"+ str(i))
        i+=1
    print("termino la ejecucion")

ejem 2

    edad=int(input("cual es tu edad"))
    while edad<0:
        print('la edad no puede ser negativa. Vuelve a intentarlo')
        edad = int(input("cual es tu edad"))
    print("gracias por colaborar. Pueda pasar")
    print("edad del aspirante "+str(edad)+ " años")

    
# uso del continue
for letra in 'python':
    if letra=="h":
        continue
    print('viendo la letra:'+letra)
# uso del else en un bucle
    email=input("introduce tu email, por favor")
    for i in email:
        if i=='@':
            arroba=True
            break
    else:
        arroba=False
    print(arroba)

    el else esta a nivel del  for y este solo se ejecutara cuando el bucle haya dado 
    la totalidad de iteraciones, es decir que cuando encuentre el caracter @ la  se saldra entonces no se ejecutara el else
 # generadores
 -> estructuras que extraen valores de una funcion y los almacenan en objetos iterables

 ## una funcion normal
    def generar_pares(limite):
        num=1
        mylist=[]
        while num<limite:
            mylist.append(num*2)
            num=num+1
        return mylist
    print(generar_pares(10))


## generador


ejem 1->devuelve toda la lista
def generar_pares(limite):
    num=1
    while num<limite:
       yield num*2
       num=num+1
devuelve_pares=generar_pares(10)

for elemento in devuelve_pares:
    print(elemento)

ejem 2 -> devuelve el primer elemento del generador, 

def generar_pares(limite):
    num=1
    while num<limite:
       yield num*2
       num=num+1
devuelve_pares=generar_pares(10)

print(next(devuelve_pares))


ejem 3->en cada llamad devuleve un elemento

def generar_pares(limite):
    num=1
    while num<limite:
       yield num*2
       num=num+1
devuelve_pares=generar_pares(10)

print(next(devuelve_pares))

print('aqui va mas codigo')
print(next(devuelve_pares))

# yield from
    def devuelve_ciudades(*ciudades):
        for elemento in ciudades:
            # for subElemento in elemento:
                yield from elemento
    ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona","Bilbao","Valencia")
    print(next(ciudades_devueltas))
    print(next(ciudades_devueltas))
# excepciones
error en tiempo de ejecucion

# captura o control de excepciones
    def divide(num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("no se puede dividir por 0")
            return "operacion erronea"
    print(divide(2,0))
    al contemplar la excepcion del error de division por cero, si se presenta el programa seguira con el resto del codigo 
    print("operacion realizada de forma exitosa")

# raise lanzar excpciones propias

    import math
    def calcula_raiz(num1):

        if num1<0:
            raise ValueError("el numero no puede ser negativo")
        else:
            return math.sqrt(num1)
    op1=(int(input("introduce un numero: ")))
    try:
        print(calcula_raiz(op1))
    except ValueError as ErrorNumeroNegativo:
        print(ErrorNumeroNegativo)

    print("programa terminado")

# POO-> PROGRAMACION ORIENTADA A OBJETOS
metodo es donde se establece el comportamiento que tendran los diferetes instancias de la clase

# crear una clase
    class Coche():
        largo_chasis=250
        ancho_chasis=120
        ruedas=4
        enmarcha=False
        
        
        def arrancar(self):
            pass
            

# objeto,instancia o ejemplar de clase

    mi_coche=Coche()

    ejemplo clase

    class Coche():
        largo_chasis=250
        ancho_chasis=120
        ruedas=4
        enmarcha=False

        def arrancar(self,arrancamos):
            self.enmarcha=arrancamos
            if (self.enmarcha):
                return 'el coche esta en marcha'
            else:
                return 'el coche esta parado'

        def estado(self):
            print("El coche tiene ", self.ruedas, " ruedas. Un ancho de", self.ancho_chasis,
                " y un largo de",self.largo_chasis)


    mi_coche=Coche()

    print(mi_coche.arrancar(True))
    mi_coche.estado()
    print("---------------------a continuacion creamos el segundo objeto-------------------")

    mi_coche2=Coche()

    print(mi_coche2.arrancar(False))
    mi_coche2.estado()
# constructor
    es un metodo especial que le da estado incial al los objetos de una clase

# encapsular
proteger una propiedad o metodo para que no se pueda acceder desde fuera de la clase se le antecede de __ nombrepropiedad o __nombremetodo
self.__ruedas = 4

# herencia
Clase padre o superclase(caracteristicas y comportamientos comunes)
clase o subclase(caracteristicas y comportamientos especificas)

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera= False
        self.frena= False

    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera=  True

    def frenar(self):
        self.frena =True
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)

class Moto(Vehiculo):
    pass

miMoto  =Moto("Honda","CBR")

miMoto.estado()

# sobre escritura de metodos
cuando una clase hija se le crea un metodo con el mismo nombre de la clase padre y este sobre escribe el metodo de la clase padre
    class Vehiculo():
        def __init__(self,marca,modelo):
            self.marca = marca
            self.modelo = modelo
            self.enmarcha=False
            self.acelera= False
            self.frena= False

        def arrancar(self):
            self.enmarcha= True

        def acelerar(self):
            self.acelera=  True

        def frenar(self):
            self.frena =True
        def estado(self):
            print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)

    class Moto(Vehiculo):
        hcaballito=''
        def caballito(self):
            self.hcaballito="estoy haciendo el caballito"
        def estado(self):
            print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena, "\n", self.hcaballito)

    miMoto  =Moto("Honda","CBR")
    miMoto.caballito()
    miMoto.estado()

# Herencia multiple
    class BicicletaElectrica(VElectricos,Vehiculos):
        pass
 al presentarse la herencia multiple se da preferencia a la primera clase que se mencione al definir la clase hija

 # herencia ->funcion super()
 
class Person():
    def __init__(self,nombre,edad,lugar_residencia):
        self.edad = edad
        self.nombre = nombre
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre, " Edad: ",self.edad ,"residencia: ",self.lugar_residencia)


class Empleado(Person):

    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,lugar_residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,lugar_residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("salario: ",self.salario, "antiguedad: ",self.antiguedad)

Antonio=Empleado(500,5,'antonio',30,'Costa Rica')
Antonio.descripcion()

# herencia->isinstance
pricipio de sustitucion ->una instancia de una subclase siempre sera una instancia
de la clase padre, pero una instacia de la clase padre no es necesariamente sera instancia de la subclase o clase hija
para comprobar si una instancia  pertenece a determinada clase

print(isinstance(Antonio,Person))
 -------------------


class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera= False
        self.frena= False

    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera=  True

    def frenar(self):
        self.frena =True
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)
class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return"la furgoneta esta cargada"
        else:
            return "la furgoneta  no esta cargada"

class Moto(Vehiculo):
    hcaballito=''
    def caballito(self):
        self.hcaballito="estoy haciendo el caballito"
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True
        if self.cargando:
            return( "estoy cargando")

class BicicletaElectrica(VElectricos,Vehiculo):
    def cargarEnergia(self):
        super().cargarEnergia()
    pass

miMoto  =Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()
mifurgoneta=Furgoneta("Renault","Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))

miBici=BicicletaElectrica("orbea","ign")
miBici.estado()

# Polimorfismo
un objeto puede cambiar  formas dependiendo del contexto en que se utilice,y al cambiar de forma tambien cambia su comportamiento

class Coche():
    def desplazamiento(self):
        print("me desplazo usando 4 ruedas")
class Moto():
    def desplazamiento(self):
        print("me desplazo usando 2 ruedas")
class Camion():
    def desplazamiento(self):
        print("me desplazo usando 6 ruedas")

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

mi_vehiculo=Coche()
desplazamiento_vehiculo(mi_vehiculo)

# uso de metodos de cadenas->string
upper
lower
capitalize()->poner primera letra en mayuscula
count()-> contar cuantas veces esta un caracter en un string
find
isdigit()->devuelve un boolean, valida si el valor es un digito o no
isalum()->comprueba si es un alfanumerico
isalpha()-> comprueba si hay solo letras
split()->separa por palabras usando espacios
strip()->borrar espacios sobrantes
replace()-> cambia una palabra o letra por otra
rfing()->representa el indice de un caracter ubicandose en el ultimo caracter

# Modulos
Es un archivo .py, sirve par organizar y reutilizar codigo
modularizacion->dividir la aplicacion en pequenos modulos o piezas

## importar el modulo

    import funciones_matematicas
    from funciones_matematicas import sumar
    from funciones_matematicas import *
    sumar(7,5)
# Paquetes

directorios don se almacena modulos relacionados entre si
se crea una carpeta que contenga en su interio un archivo __init__.py\

# archivos externos
persistecia de datos
### Fases para manejo de archivos externo
creacion->apertura->manipulacion->cierre

from  io import open
# creacion y apertura

archivo_texto=open('archivo.txt',"w")
# manipulacion
frase="estupendo dia para estudiar python \n miercoles"
archivo_texto.write(frase)
# cierre
archivo_texto.close()

# abrir un archivo en modo lectura
from  io import open
archivo_texto=open('archivo.txt',"r")
texto=archivo_texto.read()
archivo_texto.close()

# abrir un archivo modo lectura en lineas
from  io import open
archivo_texto=open('archivo.txt',"r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)->guardara el texto en un lista

# anadir mas lineas a un archivo
from  io import open
archivo_texto=open('archivo.txt',"a")
archivo_texto.write("\n siempre es una buena ocasion para estudiar python")

archivo_texto.close()
# abrir el archivo en modo lecturay escritura

# manejo de un puntero en un archivo
modificar la posicion del cursor
from  io import open

archivo_texto=open('archivo.txt',"r")

print(archivo_texto.read())

archivo_texto.seek(0)->ubica el puntero en la posicion cero, ya que despues de la primera lectura el cursor queda ubicado al final del archivo

print(archivo_texto.read())

# Serializacion
volcado de datos al fichero binario externo
guardar en tipo binario un archivo

import pickle
lista_nombres=["juan","Maria","viviana"]
fichero_binario=open("lista","wb")
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()
del(fichero_binario)->borra de memoria
------------------

carga de datos del fichero binario externo
leer desde un archivo binario
import pickle

fichero_binario=open("lista","rb")
l=pickle.load(fichero_binario)
fichero_binario.close()
print(l)

# serializar objetos
import pickle

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera= False
        self.frena= False

    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera=  True

    def frenar(self):
        self.frena =True
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)
coche1=Vehiculo("Mazda","MX5")
coche2=Vehiculo("Seat","Leon")
coche3=Vehiculo("Renaul","Megane")

coches=[coche1,coche2,coche3]
fichero=open('loscoches','wb')
pickle.dump(coches,fichero)
fichero.close()
del (fichero)

lecturaa

ficheroApertura=open("loscoches","rb")
miscoches=pickle.load(ficheroApertura)
ficheroApertura.close()
for c in miscoches:
    print(c.estado())
# intefaces graficas
librerias par trabajar con GUI 
Tkinter
WxPython
PyQT
PyGTK

from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba")
raiz.resizable(True,0)// modificar tamano de la ventana
// raiz.iconbitmap('libelula.ico') // insertar icono
raiz.geometry("650x350") estabalecer el tamano de la ventana
raiz.config(bg="purple")// color fondo de la ventana

raiz.mainloop()

## frame
mi_frame=Frame()
mi_frame.pack()
mi_frame.pack(side="right", anchor="s")
mi_frame.config(width="650", height="350")
mi_frame.config(bg="pink")

## raiz y frame
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

# label
permite mostrar texto, este texto es estatico

# funciones lambdal o anonimas
se hace  una referencia a la funcion ms no lallam

#  BBDD

import sqlite3

# crear y abrir conexion
mi_conexion=sqlite3.connect("PrimeraBase")
mi_cursor=mi_conexion.cursor()

# crear tablas
 mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20)) ")
# insertar registro
mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
mi_conexion.commit()
# cerrar conexion
mi_conexion.close()

# insertar registros por lotes

variosProductos=[
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camion",20,"Jugueteria")
]
consultas preparadas por parametros, se insertan tantos ? como campos quieras insertar

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
mi_conexion.commit()

# leer informacion de BBDD

mi_cursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=mi_cursor.fetchall()

print(variosProductos)

### ejemplo
mi_cursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=mi_cursor.fetchall()
for producto in variosProductos:
    print("Nombre Articulo:", producto[0])
mi_conexion.commit()
mi_conexion.close()

# BBDD CON CAMPO CLAVE
import  sqlite3
mi_conexion=sqlite3.connect("GestionProductos")
mi_cursor=mi_conexion.cursor()

mi_cursor.execute('''
CREATE TABLE PRODUCTOS(
CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY ,
NOMBRE_ARTICULO VARCHAR (50),
PRECIO INTEGER,
SECCION VARCHAR (20)
)
''')

productos=[
    ("AR01","pelota",20,"jugueteria"),
    ("AR02","pantalo",15,"confeccion"),
    ("AR03","destornillador",25,"ferrreteria"),
    ("AR04","jarron",45,"ceramica")
]



mi_conexion.commit()
mi_conexion.close()

# BBDD CON CAMPO CLAVE AUTOINCREMENT

import  sqlite3
mi_conexion=sqlite3.connect("GestionProductos")
mi_cursor=mi_conexion.cursor()

mi_cursor.execute('''
CREATE TABLE PRODUCTOS(
ID INTEGER PRIMARY KEY  AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR (50),
PRECIO INTEGER,
SECCION VARCHAR (20)
)
''')

productos=[
    ("pelota",20,"jugueteria"),
    ("pantalo",15,"confeccion"),
    ("destornillador",25,"ferrreteria"),
    ("jarron",45,"ceramica")
]
mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)



mi_conexion.commit()
mi_conexion.close()

# CAMPOS QUE NO SE REPITAN

NOMBRE_ARTICULO VARCHAR (50) UNIQUE

# CRUD
## CREATE
mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
## READ 
mi_cursor.execute("SELECT * FROM PRODUCTOS  WHERE SECCION='ceramica'")
productos=mi_cursor.fetchall()
print(productos)

## UPDATE
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO=35  WHERE NOMBRE_ARTICULO='pelota'")
## DELETE
mi_cursor.execute("DELETE  FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pelota'")

# consultas parametrizadas proximo 65
### ejem 1
datos = my_name.get(), my_password.get(), my_lastname.get(), my_address.get(), text_comment.get(1.0, END)

    my_cursor.execute("UPDATE DATOSUSUARIOS  SET USER_NAME=?, PASSWORD=?, LAST_NAME=?,ADDRESS=?,COMMENT=?" +
                      "WHERE ID="+my_ID.get(), (datos))
### eje 2

datos=my_name.get(),my_password.get(),my_lastname.get(),my_address.get(),text_comment.get(1.0, END)

    my_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
# funciones lambda-> funciones anonimas-on the go->on demand ->online
sintaxis mas ligera, menor tiempo

# funcion filter

def numero_par(num):
    if num %2==0:
        return True
numeros=[17,28,6,5]

print(list(filter(numero_par,numeros)))

numeros=[17,28,6,5]

print(list(filter(lambda numero_par:numero_par%

# funcion map

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{}que trabaja como {} tiene un salario de $ {}".format(self.nombre,self.cargo,self.salario)
lista_empleados=[
    Empleado("Juan","Director",750000),
    Empleado("Elsa","Administrativa",550000),
    Empleado("Oscar","Operativo",350000)
]

def calculo_comision(empleado):
    if (empleado.salario<=400000):
        empleado.salario = empleado.salario * 1.03
    return empleado
lista_empleados_comision=map(calculo_comision,lista_empleados)
for empleado in lista_empleados_comision:
    print(empleado)

# expresiones regulares o regex
 secuencia de caracteres que forma un patron de busqueda

 
import re
cadena="Vamos a aprender expresion regulares"
textoBuscar="aprender"

if re.search(textoBuscar,cadena) in not None:
    print("he encontrado 1 texto")

ejem

import re
cadena="Vamos a aprender expresion regulares"
textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
    print("he encontrado 1 texto")
else:
    print("NO he encontrado el texto")
ejm

start nos indica desde que caracter empieza a encontrase el el texto que se esta buscando

print(texto_encontrado.start())

end indica hasta  que numerdo de caracter termina  el texto que se esta buscando

 print(texto_encontrado.end())

span nos devuelve en una tupla el numero del caracter donde comienza y en donde termina el texto buscado
 print(texto_encontrado.end())
 findall busca todas las coincidencias y devuelve una lista de las mismas
cadena="Vamos a aprender expresion regulares en Python.Python es un lenguaje"
textoBuscar="Python"
print(re.findall(textoBuscar,cadena))


# decoradores
funciones que añaden funcionabilidad a otras funciones
una funcion A recibe como parametro una funcion B, y la funcion A retorna una funcion C
es decir que un decorador devuelve una funcion

def funcion_decorador_A(funcion_B):
    def funcion_C():
    # codigo de la funcion A
    return  funcion_C

# ejem

def funcion_decoradora(funcion_parametro):
    def funcion_interior():

        #Acciones adiconales que agregan

        print("Vamos a resalizar un calculo")
        funcion_parametro()

        # Acciones adiconales que agregan

        print("hemos terminado el calculo")

    return funcion_interior



como decorar una funcion
@funcion_decoradora
def suma():
    print(15+2)
    
def resta():
    print(30-10)
suma()
resta()

# funcion decorador recibe funcion con parametros

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):

        #Acciones adiconales que agregan

        print("Vamos a resalizar un calculo")
        funcion_parametro(*args)

        # Acciones adiconales que agregan

        print("hemos terminado el calculo")

    return funcion_interior



#como decorar una funcion
@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)

def resta(num1,num2):
    print(num1-num2)
suma(7,5)
resta(12,10)

# Documentacion codigo

### comentarios de multiples lineas
 """"calcula el area de un cuadrado
    recibiendo un paramentro"""

### comentarios de una sola linea

. # calcula el area del triangulo recibiendo como parametro la base y la altura

# como visualizar los comentarios en tiempo de ejecucion
print(area_cuadrado.__doc__)

otra forma

help(area_cuadrado)

## cuando la funcion esta dentro de una clase
class Areas:
    def area_cuadrado(lado):
        """"calcula el area de un cuadrado
        recibiendo un paramentro"""
        return "El area del cuadrado:" + str(lado*lado)

    def area_triangulo(base,altura):
        # calcula el area del triangulo recibiendo como parametro la base y la altura
        return "El area del triangulo es:"+str((base*altura)/2)


print(Areas.area_cuadrado(2))
help(Areas.area_cuadrado)

## realizar test para verificar funcionamiento de la "funcion" , creando un test dentro de la documentacion, saldra error en caso de que la prueba no se cumpla de lo contrario se ejecutara y no parecera nada


def area_triangulo(base,altura):
    import argparse
    """"calcula el area de un cuadrado
    recibiendo un paramentro
    
    >>> area_triangulo(5,2)
   9.0

    """
    return "El area del cuadrado:" + str((base*altura)/2)


import doctest
doctest.testmod()

ejemplo con variapruebas 

def comprueba_mail(mail_usuario):
    """
    la funcion comprueba_mail evalua un mail recibido
    verificando si tiene @. Si la arroba esta en el sitio correcto
    y que solo debe tener una @ .
    >>> comprueba_mail("juan@com.co")
    True
    >>> comprueba_mail("juancom.co@")
    False
    >>> comprueba_mail("juancom.co")
    False
    >>> comprueba_mail("juan@com#@.co")
    False

    """

    arroba=mail_usuario.count('@')
    if(arroba!=1 or mail_usuario.rfind("@")==(len(mail_usuario)-1)or mail_usuario.find("@")==0):
        return False
    else:
        return True


import doctest
doctest.testmod()

### Prueba para evaluar pruebas mas  elaboradas, donde hay expresiones anidadas y se evalua una exepcion

import math


def raiz_cuadrada (lista_numeros):
    """
    La funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametro
     en otra lista
     >>> lista = []
     >>> for i in [ 4, 9, 16 ]:
     ...  lista.append( i )
    >>> raiz_cuadrada(lista)
    [2.0, 3.0, 4.0]

     >>> lista = []
     >>> for i in [ 4, 9, -16, 90 ]:
     ...  lista.append( i )
    >>> raiz_cuadrada(lista)
    Traceback (most recent call last):
     ...
    ValueError: math domain error
    """
    return [math.sqrt(n) for n in lista_numeros]


print ( raiz_cuadrada( [ 9, 16, 25 ] ) )


import doctest
doctest.testmod()
# Crear un ejecutable
pip install pyintaller
una vez unibicado en la carpeta donde tienes archivo que quiere convertir en ejecutabl
 ejecutar pypinstaller --window --onefile --icon=./nombreimagen.ico nombredelarchivo.py


