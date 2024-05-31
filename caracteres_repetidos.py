"""Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.
Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.
"""
   
def contar_caracteres_repetidos(cadena:str)->int:
    repetidos = 0
    rep = ""
    aux = ""                                       
    for i in cadena:
        if i in cadena:                           
            if i not in rep:                         
                rep += i                             
            else:
                if i not in aux:
                    aux += i 
                    repetidos += 1

    return repetidos

print(contar_caracteres_repetidos("messiass"))