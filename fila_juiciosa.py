"""
Andrés es un profesor que tiene la teoría de que hay filas del salón que tienen mejor promedio que otras.
Para comprobarlo, ha decidido crear una función que calcule el promedio de la nota de una fila. La función recibe como parámetros una matriz, un número de fila y retorna el promedio de la fila redondeado a dos decimales.
Cuidado: un 0 en la matriz no significa que el estudiante haya sacado 0, sino que no hay ningún estudiante en dicha silla.
Tenga muy en cuenta que para Andrés la primera fila es la número 1. Si se pide un número de fila que no tenga sentido, su función debe retornar -1. Si la fila no tiene estudiantes, su función debe retornar 0.  
"""

def promedio_fila(matriz:list,fila:int)->float:
    promedio = 0.0
    cont_est = 0
    aux = 0
    if len(matriz)<fila or fila<=0:
        return -1
    for i in range(0,len(matriz[0])):
        if matriz[fila-1][i]>0:
            cont_est += 1
            promedio += matriz[fila-1][i]
        elif matriz[fila-1][i]==0:
            aux += 1
    if aux == len(matriz[fila-1]):
        return 0
         
    return round(float(promedio/cont_est),2)  