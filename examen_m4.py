"""
Estadísticas de descargas
Descripción del problema

Una plataforma web que vende y distribuye modelos tridimensionales 
para su uso en proyectos de arquitectura tiene información sobre cada 
venta  que han tenido los modelos publicados. A partir de esa 
información, ellos quieren que tú los ayudes a calcular estadísticas 
sobre cada modelo.
Tu tarea será construir la función calcular_estadisticas que recibe 
un DataFrame con la información de las descargas y retorna un DataFrame 
con las estadísticas.

El DataFrame de entrada tendrá una fila con la información de cada 
descarga: el nombre del modelo descargado, el nombre del usuario que la 
descargó, el dinero en dólares que pagó por el modelo (número decimal), 
la cantidad de estrellas (entre 1 y 5) que el usuario le dio al modelo 
(número decimal) y si dejó o no un comentario sobre el modelo después de
 haberlo descargado (valor booleano). El precio de un modelo particular 
podría ser diferente entre descargas porque la plataforma suele hacer 
promociones y porque los artistas que los crean pueden modificar el 
precio cuando ellos quieran. El precio podría ser 0 en algunas 
descargas, pero esos registros no se deberá tener en cuenta.

El siguiente es un ejemplo de un DataFrame que muestra los nombres de
las columnas y posibles valores que puede haber en el DataFrame.

El DataFrame que retorna la función tiene que tener una fila por cada
 modelo. El DataFrame tendrá 7 columnas: CANTIDAD, que tendrá un número 
entero con la cantidad de descargas que haya tenido el modelo; PROMEDIO,
 que tendrá un número decimal con la cantidad promedio que se pagó por 
el modelo; MAXIMO que tendrá un número decimal con la cantidad máxima 
que se pagó por el modelo; MINIMO que tendrá un número decimal con la 
cantidad mínima que se pagó por el modelo; ESTRELLAS, que tendrá un 
número decimal con la cantidad promedio de estrellas que se le dio al 
modelo; DESV. ESTRELLAS, que tendrá un número decimal con la desviación 
estándar de la cantidad de estrellas que se le hayan dado al modelo; y 
COMENTARIOS, que tendrá un número entero con la cantidad de comentarios 
que hayan dejado los compradores.

Notas importantes sobre el DataFrame resultado:

El índice del DataFrame tendrá los nombres de los modelos y sólo 
deben aparecer aquellos para los que al menos un usuario haya pagado. Es
 decir que no deben aparecer los modelos que hayan sido siempre 
gratuitos.
Los modelos deben aparecer en orden alfabético de acuerdo a su nombre.
Todos los números que no sean enteros deben aparecer redondeados a dos cifras decimales.
Como la desviación estándar no se puede calcular cuando haya
sólo un dato, en lugar de NaN debe aparecer 0.0 en el resultado.
"""

import pandas as pd
import numpy as np

def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame:
    # Filtrar las descargas donde el PAGO sea mayor que 0
    descargas = descargas[descargas['PAGO'] > 0]
    
    # Definir una función para calcular la desviación estándar de las calificaciones de estrellas
    def calcular_desviacion_std(x):
        if len(x) > 1:
            return np.std(x, ddof=1)  # Usar ddof=1 para la desviación estándar muestral
        else:
            return 0.0
    
    # Definir las funciones de agregación para cada columna requerida
    agg_functions = {
        'PAGO': ['count', 'mean', 'max', 'min'],
        'ESTRELLAS': ['mean', calcular_desviacion_std],
        'COMENTARIO': 'sum'
    }
    
    # Agrupar por MODELO y aplicar las funciones de agregación
    stats = descargas.groupby('MODELO').agg(agg_functions)
    
    # Renombrar las columnas según las especificaciones
    stats.columns = ['CANTIDAD', 'PROMEDIO', 'MAXIMO', 'MINIMO', 'ESTRELLAS', 'DESV. ESTRELLAS', 'COMENTARIOS']
    
    # Redondear los valores a dos cifras decimales
    stats = stats.round(2)
    
    # Ordenar alfabéticamente por el nombre del modelo
    stats = stats.sort_index()
    
    # Convertir el índice a columnas para cumplir con el formato requerido
    stats = stats.reset_index()
    
    # Establecer el índice como el nombre del modelo
    stats = stats.set_index('MODELO')
    
    return stats
