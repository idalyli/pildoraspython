
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



