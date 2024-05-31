def mismos_digitos(a:int,b:int)->bool:
    digitos_numero1 = set(str(a))
    digitos_numero2 = set(str(b))
    bandera = False
    # Comprueba si los conjuntos de dígitos son iguales
    #return digitos_numero1 == digitos_numero2
    if len(digitos_numero1)>len(digitos_numero2):
        mayor = digitos_numero1
        menor = digitos_numero2
    else:
        mayor = digitos_numero2
        menor = digitos_numero1
    for i in mayor:
        if i in menor:
            bandera = True
        else:
            return False
    return bandera

print(mismos_digitos(2,8))