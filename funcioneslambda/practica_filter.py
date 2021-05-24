# def numero_par(num):
#     if num %2==0:
#         return True
# numeros=[17,28,6,5]
#
# print(list(filter(numero_par,numeros)))

numeros=[17,28,6,5]

print(list(filter(lambda numero_par:numero_par%2==0,numeros)))

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
    Empleado("Oscar","Operati",350000)
]

salarios_altos=filter(lambda empleado:empleado.salario>500000,lista_empleados)
for empleado_salario in salarios_altos:
    print(empleado_salario)