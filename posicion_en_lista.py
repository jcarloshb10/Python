"""
Escriba una función que reciba una lista y un número entero a buscar, y que retorne un entero que indique el índice en que se encuentra este elemento.
En caso de que el elemento se encuentre más de una vez dentro de la lista, debe retornar la primera posición en que lo encuentre.
En caso de no encontrar el número, retorne -1.
"""

def buscar_elemento(entrada:list,buscado:int)->int:
    cont = 0
    for i in entrada:
        cont = cont +1
        if buscado == i:
            return cont
    return -1