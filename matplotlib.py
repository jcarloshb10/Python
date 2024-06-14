import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def cargar_imagen(ruta_imagen:str)->list:
    imagen = mpimg.imread(ruta_imagen).tolist()
    return imagen

def visualizar_imagen(imagen:list)->None:
    plt.imshow(imagen)
    plt.show()

def convertir_negativo(imagen:list)->list:
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            pixel = imagen[i][j]
            for k in range(3):
                imagen[i][j][k] = abs(pixel[k]-1.0)
    return imagen