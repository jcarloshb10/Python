"""
Un hacker alteró los resultados de los partidos de un torneo suramericano de fútbol y ahora la CONMEBOL tiene que hacer algo para corregir la información averiada. Escriba una función que reciba la información con problemas en un DataFrame y retornará otro DataFrame con la información corregida.
El DataFrame que se recibe tiene siguientes columnas: 
'local': el nombre del equipo local en cada partido.
'visitante': el nombre del equipo visitante en cada partido.
'goles_local': la cantidad de goles que anotó el equipo local en cada partido.
'goles_visitante': la cantidad de goles que anotó el equipo visitante en cada partido.
'resultado': el resultado del partido, es decir el nombre del equipo ganador o la cadena 'empate' en caso de que hayan anotado la misma cantidad de goles.
Durante el análisis del ataque informático, la CONMEBOL descubrió que el hacker sólo realizó 3 tipos de daños:
Alteró la columna 'resultado' de forma aleatoria.
Introdujo valores nulos en la cantidad de goles, tanto de los equipos locales como de los visitantes.
Alteró los nombres de los equipos.
Según lo que decidió la CONMEBOL, la función debe corregir estos errores de la siguiente manera:
En la columna 'resultado' debe quedar el resultado correcto del partido (el nombre del equipo ganador o la cadena 'empate').
Debe remplazar las cantidades de goles por 0 cuando se encuentren valores nulos.
Debe eliminar los partidos en los cuales aparezca que un equipo jugó contra él mismo.
Los valores del DataFrame resultante deben tener el mismo orden en el que se recibieron originalmente.
"""

import pandas as pd
import numpy as np

def depurar_partidos(partidos):
    # Paso 1: Reemplazar valores nulos en goles_local y goles_visitante por 0
    partidos['goles_local'].fillna(0, inplace=True)
    partidos['goles_visitante'].fillna(0, inplace=True)
    
    # Paso 2: Eliminar partidos donde un equipo juega contra sí mismo
    partidos = partidos[partidos['local'] != partidos['visitante']]
    
    # Función para corregir el resultado basado en los goles
    def corregir_resultado(row):
        goles_local = row['goles_local']
        goles_visitante = row['goles_visitante']
        
        if goles_local > goles_visitante:
            return row['local']  # Local es el ganador
        elif goles_local < goles_visitante:
            return row['visitante']  # Visitante es el ganador
        else:
            return 'empate'  # Empate cuando los goles son iguales
    
    # Corregir la columna 'resultado' basándose en los goles
    partidos['resultado'] = partidos.apply(corregir_resultado, axis=1)
    
    # Mantener el orden original del DataFrame
    partidos.reset_index(drop=True, inplace=True)
    
    return partidos
