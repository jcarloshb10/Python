"""
Catalina necesita llevar un mejor control de sus gastos cuando hace mercado. Para esto, ha decidido construir una aplicación para registrar cada producto que agregue en su carrito de compras. Estos datos son guardados en un diccionario cuyas llaves corresponden a los nombres de los productos. El valor asociado a cada llave es el precio del producto correspondiente.
Cree una función que retorne el valor total del carrito de compras. Esto es, la suma de los precios individuales de todos los productos que están en el carrito.  
"""

def total_carrito(carrito_compras:dict)->str:
    total = 0
    for art in carrito_compras.values():
        total += art
    return total

carrito_compras = {'bananos': 2400, 'chocolatinas': 1300, 'detergente': 4000}
print(total_carrito(carrito_compras))