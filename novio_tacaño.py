"""
Nicolás es un novio muy amoroso, pero tiene fama de ser tacaño. Para el cumpleaños de su novia ha pedido un catálogo de artículos para escoger el regalo más barato disponible. El catálogo es un diccionario que tiene varias llaves que corresponden al nombre de los productos. El valor asociado a cada llave es el precio del producto.
Cree una función que retorne el nombre del artículo más barato en el catálogo.
Si Nicolás encuentra dos artículos igual de baratos, comprará el que tenga el nombre alfabéticamente menor (el que aparecería antes en el diccionario ignorando las mayúsculas y minúsculas).
Si el artículo más barato vale más de 10.000 pesos, Nicolás no comprará nada e invitará a su novia a ver una película en su casa.  
"""

def producto_mas_barato(catalogo: dict) -> str:
    articulo = None
    barato = float('inf')  # Inicializar con infinito para garantizar que cualquier precio sea menor
    if len(catalogo) == 0:
        return "No hay productos para escoger"
    else:
        for nombre in catalogo:
            precio = catalogo[nombre]
            if precio < barato:
                barato = precio
                articulo = nombre
            elif precio == barato:
                if nombre.lower()<articulo.lower():
                    barato = precio
                    articulo = nombre
    if barato>=10000:
        return None
    return articulo

