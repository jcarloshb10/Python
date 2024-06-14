"""
Pregunta 5
Moda en una cadena


Descripción del problema

En este ejercicio deberás identificar la letra más común (o moda) en una cadena recibida por parámetro. Crea una función que reciba una cadena (str) que será analizada, y que retorne otra cadena (str) que contenga la letra más común en la cadena inicial.

Para tu facilidad, las cadenas que recibirás solo contendrán letras mayúsculas y no tendrán tildes o acentos. No obstante, estas pueden tener espacios, puntos y comas.

En caso de que haya 2 letras con la misma cantidad de apariciones, debes retornar la que sea alfabéticamente posterior.
"""

def letra_mas_comun(cadena: str) -> str:
    encontrada = {}
    lista = list(cadena)
    for i in lista[:]:  # Utilizamos una copia de la lista para evitar problemas al modificarla
        if i == " " or i == "," or i == ".":
            lista.remove(i)
        else:
            if i in encontrada:
                encontrada[i] += 1
            else:
                encontrada[i] = 1
    cad = max(encontrada.keys(), key=lambda x: (encontrada[x], x))
    return cad

print(letra_mas_comun("A VER SI ESTO ES DE TU TALLA, AMIGA ENORME"))

