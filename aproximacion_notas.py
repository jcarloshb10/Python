"""Una clase de la Universidad de los Andes tiene las siguientes reglas con respecto a las aproximaciones de las notas finales.  
Si la nota es mayor o igual a 4.5, la nota se aproxima a 5.0.
Si la nota es mayor o igual a 3.5 y menor a 4.5, la nota se aproxima a 4.0.
Si la nota es mayor o igual a 2.5 y menor a 3.5, la nota se aproxima a 3.0.
De lo contrario, la nota asignada será 1.5.  
Teniendo una lista de diccionarios en donde cada uno corresponde a un estudiante y que tiene como llaves "nombre" y "nota" (sin aproximar), retorne una lista con todos los diccionarios actualizados con sus notas después de aproximación."""

def calcular_definitivas(estudiantes: list) -> list:
    lista = []
    for estudiante in estudiantes:
        if float(estudiante["nota"]) >= 4.5:
            lista.append({"nombre": estudiante["nombre"], "nota": 5.0})
        elif float(estudiante["nota"]) >= 3.5 and float(estudiante["nota"]) < 4.5:
            lista.append({"nombre": estudiante["nombre"], "nota": 4.0})
        elif float(estudiante["nota"]) >= 2.5 and float(estudiante["nota"]) < 3.5:
            lista.append({"nombre": estudiante["nombre"], "nota": 3.0})
        else:
             lista.append({"nombre": estudiante["nombre"], "nota": 1.5})
    return lista

# Ejemplo de lista de estudiantes
lista_estudiantes = [
    {"nombre": "Juan", "nota": 4.5},
    {"nombre": "María", "nota": 3.8},
    {"nombre": "Pedro", "nota": 4.7}
]

print(calcular_definitivas(lista_estudiantes))
