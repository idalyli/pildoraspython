

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