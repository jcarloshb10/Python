"""Catalina necesita llevar un mejor control de sus gastos cuando hace mercado. 
Para esto, ha decidido construir una aplicación para registrar cada producto que agregue en su carrito de compras. 
Estos datos son guardados en un diccionario cuyas llaves corresponden a los nombres de los productos. 
El valor asociado a cada llave es el precio del producto correspondiente.
Cree una función que retorne el nombre del producto más costoso del carrito de compras. 
Si se encuentran dos productos igual de costosos (siendo los más costosos del carro), la función retorna el menor alfabéticamente. 
Por ejemplo, si los 'bananos' que compra Catalina costaran los mismo que las 'chocolatinas', la función retornaría 'bananos'  """

def producto_mas_costoso(carrito_compras:dict)->str:
    articulo = None
    caro = 0  # Inicializar con infinito para garantizar que cualquier precio sea menor
    if len(carrito_compras) == 0:
        return "No hay productos en el carrito"
    else:
        for nombre in carrito_compras:
            precio = carrito_compras[nombre]
            if precio > caro:
                caro = precio
                articulo = nombre
            elif precio == caro:
                if nombre<articulo:
                    caro = precio
                    articulo = nombre
    return articulo

carrito_compras = {'chocolatinas': 1300, 'bocadillos': 1300, 'galletas': 700}
print(producto_mas_costoso(carrito_compras))