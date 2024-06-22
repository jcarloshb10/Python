"""
Construya una función que reciba un DataFrame con información sobre el desempeño de un conjunto de estudiantes en 5 materias y retorne un DataFrame con información sobre los mejores estudiantes.
El DataFrame que recibe la función tiene 6 columnas: 'nombre', donde aparecen los nombres de los estudiantes, 'matematicas', 'ingles', 'ciencias', 'literatura' y 'arte', en las cuales aparecen las calificaciones de los estudiantes en cada una de esas materias. Las calificaciones son números decimales entre 0 y 5.0.
La función debe retornar un DataFrame con dos columnas: 'nombre', donde aparecen los nombres de los estudiantes; y 'promedio', donde aparecen los promedios de sus calificaciones redondeados a dos decimales. El DataFrame resultante, debe estar ordenado de mayor a menor promedio y solo deben aparecer los estudiantes cuyo promedio haga parte del mejor 25%.
Nota: para ordenar los resultados y seleccionar el mejor 25%, no tenga en cuenta las aproximaciones.
"""

import pandas as pd

def mejores_estudiantes(estudiantes):
    # Calcular el promedio por estudiante y redondear a dos decimales
    estudiantes['promedio'] = estudiantes[['matematicas', 'ingles', 'ciencias', 'literatura', 'arte']].mean(axis=1).round(2)
    
    # Ordenar por promedio en orden descendente
    estudiantes = estudiantes.sort_values(by='promedio', ascending=False)
    
    # Calcular cuántos estudiantes corresponden al 25%
    cantidad_top_25 = int(len(estudiantes) * 0.25)
    
    # Seleccionar los mejores estudiantes (el 25% superior)
    mejores_estudiantes = estudiantes.head(cantidad_top_25)
    
    # Retornar solo las columnas 'nombre' y 'promedio' ordenadas por promedio descendente
    return mejores_estudiantes[['nombre', 'promedio']]

# Ejemplo de uso:
# Supongamos que 'df' es tu DataFrame con las calificaciones
# df = pd.DataFrame({
#     'nombre': ['Juan', 'Ana', 'Pedro', 'María', 'Luis'],
#     'matematicas': [4.5, 3.2, 5.0, 4.1, 3.9],
#     'ingles': [3.8, 4.5, 4.0, 3.7, 4.2],
#     'ciencias': [4.2, 4.1, 3.9, 4.4, 3.8],
#     'literatura': [3.9, 4.3, 4.5, 3.8, 4.1],
#     'arte': [4.1, 4.2, 3.8, 4.0, 4.3]
# })

# Llamar a la función para obtener los mejores estudiantes
# mejores = mejores_estudiantes(df)
# print(mejores)
