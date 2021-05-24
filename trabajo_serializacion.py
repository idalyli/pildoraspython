import pickle

fichero_binario=open("lista","rb")
l=pickle.load(fichero_binario)
fichero_binario.close()
print(l)