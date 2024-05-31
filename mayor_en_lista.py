"""
Escriba una función que encuentre el mayor número en una lista de enteros positivos.
En caso de que la lista esté vacía, se debe retornar-1.  
"""

def encontrar_mayor(entrada:list)->int:
    resul = -1
    mayor = -1
    for i in entrada:
        if i > mayor:
            mayor = i
    return mayor