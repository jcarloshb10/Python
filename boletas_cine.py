"""Tus amigos, a quienes también les gusta mucho ver películas, te han propuesto ir al cine la próxima semana y quieren conocer los precios de las boletas.

Estas son las tarifas básicas de acuerdo con el tipo de sala:

Dinamix - 18800 pesos

3D - 15500 pesos

2D - 11300 pesos.

El cinema tiene, además, varias promociones que aplican para calcular el precio de las boletas que dependen del tipo de sala, del número de boletas que se compren simultáneamente, de la hora del día, del tipo de pago (tarjeta del cinema u otros medios de pago) y de si se tenía reserva.

Las promociones son las siguientes:

En las horas menos congestionadas (horas no pico) todas las salas tienen un descuento del 10% sobre la tarifa básica y si se compran 3 o más boletas, se aplican $500 pesos más de descuento por cada boleta

Si el medio de pago es la tarjeta del cinema, se hace un 5% descuento calculado sobre la tarifa básica

Cuando se hace una reserva, se tiene un recargo de $2000 pesos por boleta sin importar el tipo de sala

En las horas pico, la tarifa básica se incrementa un 25% para las salas 2D y 3D y un 50% para la sala Dinamix (este aumento no se tiene en cuenta para los recargos y descuentos).

Debes escribir una función que calcule cuánto te costarán las boletas para ti y tus amigos."""

def calcular_costo_boletas(cantidad_boletas:int,tipo_sala:str,hora_pico:bool,pago_tarjeta_cinema:bool,reserva:bool)->int:
    precio_basico = 0
    if tipo_sala=="2D":
        precio_basico = 11300
    elif tipo_sala=="3D":
        precio_basico = 15500
    else:
        precio_basico = 18800
    precio = cantidad_boletas * precio_basico
    if not hora_pico:
        precio = precio - ((precio * 10)/100)
        if cantidad_boletas>=3:
            precio = precio - (cantidad_boletas*500)
    else:
        if tipo_sala == "2D" or tipo_sala == "3D":
            precio = precio + ((precio*25)/100)
        else:
            precio = precio + ((precio*50)/100)
    if pago_tarjeta_cinema:
        precio = precio - ((precio*5)/100)
    if reserva:
        precio = precio + (cantidad_boletas*2000)
    #print(precio)
    return int(round(precio,0))

#print(calcular_costo_boletas(3,"2D",False,False,False))