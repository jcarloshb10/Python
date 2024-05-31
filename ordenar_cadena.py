def ordenar_cadena(cadena: str) -> str:
    # Convertir la cadena a una lista de caracteres y ordenarla
    lista_ordenada = sorted(cadena)
    # Unir la lista ordenada de caracteres en una cadena nuevamente
    cadena_ordenada = ''.join(lista_ordenada)
    return cadena_ordenada

print(ordenar_cadena("roma"))