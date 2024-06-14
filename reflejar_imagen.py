"""
En este ejercicio se debe reflejar la imagen verticalmente sobre una  línea imaginaria en el centro de la figura, creando una imagen espejo de  la figura original. En cada posición de la matriz que representa la  imagen hay una tupla de 3 flotantes entre 0 y 1 que representan los  valores R, G y B del píxel.
Después de reflejar una figura, la distancia  entre la línea de reflexión y cada punto en la figura original es la  misma que la distancia entre la línea de reflexión y el punto  correspondiente en la imagen de espejo. Para hacer esta transformación,  se intercambian las columnas de píxeles de la imagen: La primera con la  última, la segunda con penúltima, etc.
"""

def reflejar_imagen_verticalmente(imagen:list)->list:
    alto = len(imagen)
    ancho = len(imagen[0])
    # Crear la matriz sin valores
    matriz = [[0] * ancho for _ in range(alto)]
    for i in range(alto):
        for j in range(ancho):
            r,g,b = imagen[i][j]
            matriz[i][ancho-j-1]=(r,g,b)
    return matriz