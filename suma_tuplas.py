"""
Construya una función que reciba dos vectores (con 3 componentes cada uno) y retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla con tres valores flotantes.
"""

def suma_vectorial(vector_1:tuple,vector_2:tuple)->tuple:
    x,y,z=vector_1
    x2,y2,z2=vector_2
    tupla = (x+x2,y+y2,z+z2)
    return tupla