import re
def analizar_texto(texto: str, caracteres_permitidos: list) -> dict:
    if texto=="":
        return {}
    # Creamos un diccionario para almacenar las palabras y sus detalles
    palabras = {}
    # Convertimos el texto a minúsculas para evitar duplicados por mayúsculas/minúsculas
    texto = texto.lower()
    # Removemos los caracteres no permitidos del texto
    texto = ''.join(caracter for caracter in texto if caracter in caracteres_permitidos or caracter in [' ', ',','.'])
    # Dividimos el texto en palabras utilizando espacios en blanco como separadores
    palabras_texto = re.split(r'[,. ]', texto)
    # Inicializamos una variable para mantener el índice actual en el texto original
    indice_actual = 0
    # Iteramos a través de cada palabra en el texto
    for palabra in palabras_texto:
        inicio_palabra = texto.find(palabra, indice_actual)
        fin_palabra = inicio_palabra + len(palabra)
        # Si la palabra ya está en el diccionario, actualizamos sus detalles
        if palabra in palabras:
            apariciones, primera_aparicion, ultima_aparicion = palabras[palabra]
            apariciones += 1
            palabras[palabra] = (apariciones, primera_aparicion, inicio_palabra)
        # Si la palabra es nueva, la añadimos al diccionario
        else:
            palabras[palabra] = (1, inicio_palabra, inicio_palabra)
        # Actualizamos el índice actual para la próxima búsqueda
        indice_actual = fin_palabra
    for i in list(palabras):
        if i == '':
            del palabras[i]
    
    return palabras

texto = "Seis suecos sosos secan sesos sin sal, Secan seis sesos los suecos, Salan seis sesos con sal, secan y salan los sesos, que sacan del secadal."
caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']

print(analizar_texto(texto, caracteres_permitidos))

texto = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
caracteres_permitidos = ['*']
print(analizar_texto(texto,caracteres_permitidos))

