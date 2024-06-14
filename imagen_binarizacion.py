"""
Este ejercicio consiste en llevar los valores de una matriz que  representa una imagen a dos colores: negro y blanco. En cada posición de  la matriz que representa la imagen, hay una tupla de 3 flotantes entre 0 y 1 que representan los valores R, G y B del píxel. 
Para ello, se establece un umbral (valor entre 0 y 1) y los  píxeles con promedio de color que  son iguales o mayores al  umbral se cambian a blanco (todos los valores de la tupla en 1) y los que están por  debajo se cambian a negro (todos los valores de la tupla en 0).
"""

def binarizar_imagen(imagen:list,umbral:float)->list:
    alto = len(imagen)
    ancho = len(imagen[0])
    # Crear la matriz sin valores
    matriz = [[0] * ancho for _ in range(alto)]
    for i in range(alto):
        for j in range(ancho):
            r,g,b = imagen[i][j]
            promedio = float((r+g+b)/3)
            if promedio >= umbral:
                r=1
                g=1
                b=1
                matriz[i][j]=(r,g,b)
            else:
                r=0
                g=0
                b=0
                matriz[i][j]=(r,g,b)
    return matriz