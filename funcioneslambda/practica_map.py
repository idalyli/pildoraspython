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