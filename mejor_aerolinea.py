"""
Recopilamos los registros de los vuelos que ocurrieron durante un día entre aeropuertos ubicados en Estados Unidos y los organizamos en un diccionario de diccionarios. Ahora queremos que usted nos ayude a averiguar cuál es la mejor aerolínea con base en la puntualidad. Es decir, queremos saber cuál es la aerolínea que acumuló el menor retraso promedio en los vuelos que recopilamos.
El parámetro vuelos de la función, es un diccionario de diccionarios con la información de los vuelos.
Las llaves en este diccionario son el código de cada vuelo.
Los valores en este diccionario son diccionarios con la información de un vuelo organizado de acuerdo con las siguientes llaves:
aerolinea, corresponde al nombre de la aerolínea.
origen, corresponde al código de aeropuerto de origen.
destino, corresponde al código de aeropuerto destino del vuelo.
distancia, corresponde a la distancia entre el origen y el destino.
retraso, corresponde a la cantidad de minutos de retraso que tuvo el vuelo.
duracion, corresponde a la duración planeada del vuelo en minutos.
salida, corresponde a un entero que representa la hora de salida.
La hora de salida, se representa usando la hora en formato 24 horas multiplicada por 100 más la cantidad de minutos (por ejemplo, las 2007 indica que el vuelo salió a las 8:07 pm).  
"""

def mejor_aerolinea(vuelos:dict)->str:
    mejor_aero = ""
    retraso = float("inf")
    aux_retraso = {}
    for codigo in vuelos:
        vuelo = vuelos[codigo]
        aero = vuelo["aerolinea"]
        retraso = vuelo["retraso"]
        if aero in aux_retraso:
            aux_retraso[aero] += retraso
        else:
            aux_retraso[aero] = retraso
    mejor_aero = min(aux_retraso, key=aux_retraso.get)
    return mejor_aero

