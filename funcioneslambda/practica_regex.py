import re
# cadena="Vamos a aprender expresion regulares"
# textoBuscar="aprender"

# if re.search(textoBuscar,cadena) is not None:
#     print("he encontrado 1 texto")
# else:
#     print("NO he encontrado el texto")
# texto_encontrado=re.search(textoBuscar,cadena)
# # start nos indica desde que caracter empieza a encontrase el el texto que se esta buscando
# print(texto_encontrado.start())
# # end indica hasta  que numerdo de caracter termina  el texto que se esta buscando
# print(texto_encontrado.end())
# # span nos devuelve en una tupla el numero del caracter donde comienza y en donde termina el texto buscado
# print(texto_encontrado.end())
# findall busca todas las coincidencias y devuelve una lista de las mismas
# cadena="Vamos a aprender expresion regulares en Python.Python es un lenguaje"
# textoBuscar="Python"
# print(re.findall(textoBuscar,cadena))


# ------------ejemplo metacaracteres anclas-------------
#metacaracter ^ busca coincidencias que inicien con el parametro de busqueda que selecciones
#metacaracter $ busca coincidencias del texto que finalice con el parametro de busqueda que selecciones

lista_nombres=["Ana Gomez","Maria Martin","Sandra Lopez", "Santiago Martin"]
for elemento in lista_nombres:
    # if re.findall('^San',elemento):
    #     print(elemento)
    if re.findall('Martin$',elemento):
        print(elemento)


