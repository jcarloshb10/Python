def sucesion_fibonacci(cantidad_numeros:int)->str:
    cadena = ""
    if cantidad_numeros <= 0:
        return cadena
    
    numero1 = 0
    numero2 = 1
    cadena += str(numero1)
    for i in range(1, cantidad_numeros):
        cadena += ","
        cadena += str(numero2)
        numero_temp = numero1 + numero2
        numero1 = numero2
        numero2 = numero_temp
    
    return cadena

print(sucesion_fibonacci(10))