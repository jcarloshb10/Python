"""
Construya la función calcular_habitantes_por_puesto que calcule la cantidad de habitantes que hay en un país, por cada estudiante inscrito en una universidad de ese país y clasificada en el ranking TIMES.
La función recibe dos DataFrames. El primero tiene la información sobre la población de cada país organizada en tres columnas: 'Pais', 'Poblacion' y 'Edad_mediana'. El segundo tiene la información sobre universidades organizada en tres columnas: 'country', con el nombre del país; 'university_name', con el nombre de una universidad del ranking; y 'num_students', con el número de estudiantes inscritos en esa universidad.
Su función debe retornar un DataFrame con las siguientes condiciones:
Una columna llamada 'Pais' con el nombre de los países.
Una columna llamada 'habitantes_por_puesto'. 
En esta última columna aparecerá la cantidad de habitantes de cada país, dividida por la cantidad total de estudiantes que hay en las universidades del país que aparecen en el ranking TIMES. Por ejemplo, si la población de Australia es de 25 millones de personas y hay 31 universidades que en total atienden a 740.000 estudiantes, entonces la cantidad de 'habitantes_por_puesto' será 33.8 (el número debe redondearse a 1 cifra decimal). Además, el DataFrame resultante debe estar ordenado de menor a mayor de acuerdo con la cantidad de 'habitantes_por_puesto'.
Nota: para ordenar los resultados no tenga en cuenta las aproximaciones.
"""

import pandas as pd

def calcular_habitantes_por_puesto(poblacion, universidades):
    # Paso 1: Calcular el total de estudiantes por país
    estudiantes_por_pais = universidades.groupby('country')['num_students'].sum().reset_index()
    estudiantes_por_pais.rename(columns={'country': 'Pais'}, inplace=True)
    
    # Paso 2: Combinar con el DataFrame de población para calcular habitantes por puesto
    datos_combinados = pd.merge(poblacion, estudiantes_por_pais, on='Pais', how='inner')
    datos_combinados['habitantes_por_puesto'] = datos_combinados['Poblacion'] / datos_combinados['num_students']
    
    # Redondear a 1 decimal
    datos_combinados['habitantes_por_puesto'] = datos_combinados['habitantes_por_puesto'].round(1)
    
    # Seleccionar las columnas requeridas y ordenar correctamente
    resultado = datos_combinados[['Pais', 'habitantes_por_puesto']].sort_values(by='habitantes_por_puesto', ascending=True)
    
    # Verificar que el DataFrame está ordenado correctamente
    assert (resultado['habitantes_por_puesto'].diff().fillna(0) >= 0).all(), "El DataFrame no está ordenado correctamente"
    
    return resultado
