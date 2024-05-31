"""El mejor estudiante de cada curso

Descripción del problema

Los estudiantes de un cierto colegio tienen que ver 5 cursos: Matemáticas, Español, Ciencias, Literatura y Arte. 
La información de cada estudiante se representará usando un diccionario con 6 llaves: "nombre", que tendrá asociado el nombre del estudiante; 
"matematicas", que tendrá asociada la nota del estudiante en el curso Matemáticas; "español", que tendrá asociada la nota del estudiante en 
el curso Español; "ciencias", que tendrá asociada la nota del estudiante en el curso Ciencias; "literatura", que tendrá asociada la nota del 
estudiante en el curso Literatura; y "arte", que tendrá asociada la nota del estudiante en el curso Arte. Las notas son números decimales 
entre 0 y 5.

Tu función debe retornar un diccionario con las llaves "matematicas", "español", "ciencias", "literatura" y "arte". Cada llave debe tener 
asociado el nombre del estudiante que tenga la mejor nota en el curso correspondiente. Si hay dos o más estudiantes que comparten el mejor 
promedio en algún caso, debes escoger el estudiante que tenga el nombre alfabéticamente menor (el que aparecería primero en un diccionario 
(de lenguaje hablado y escrito, no el tipo de dato en Python), independientemente de mayúsculas o minúsculas"""

def mejor_de_cada_curso(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:dict,estudiante5:dict)->dict:

    mejores_notas = {
        "matematicas": "",
        "espanol": "",
        "ciencias": "",
        "literatura": "",
        "arte": ""
    }

    for curso in mejores_notas.keys():
        mejor_estudiante = {"nombre": "", "nota": -1}
        for estudiante in [estudiante1,estudiante2,estudiante3,estudiante4,estudiante5]:
            nota = estudiante[curso]
            if nota > mejor_estudiante["nota"]:
                mejor_estudiante["nombre"] = estudiante["nombre"]
                mejor_estudiante["nota"] = nota
            elif nota == mejor_estudiante["nota"]:
                # Si dos estudiantes tienen la misma nota, se elige el nombre alfabéticamente menor
                if estudiante["nombre"].lower() < mejor_estudiante["nombre"].lower():
                    mejor_estudiante["nombre"] = estudiante["nombre"]
                    mejor_estudiante["nota"] = nota
        mejores_notas[curso] = mejor_estudiante["nombre"]

    return mejores_notas

"""estudiante1 = {"nombre": "Juan", "matematicas": 4.5, "espanol": 3.2, "ciencias": 4.8, "literatura": 4.0, "arte": 3.9}
estudiante2 = {"nombre": "Maria", "matematicas": 3.9, "espanol": 4.8, "ciencias": 4.5, "literatura": 4.2, "arte": 4.1}
estudiante3 = {"nombre": "Pedro", "matematicas": 4.8, "espanol": 4.2, "ciencias": 4.7, "literatura": 4.6, "arte": 4.3}
estudiante4 = {"nombre": "Andrea", "matematicas": 3.9, "espanol": 4.8, "ciencias": 4.5, "literatura": 4.2, "arte": 4.1}
estudiante5 = {"nombre": "Berta", "matematicas": 4.8, "espanol": 4.2, "ciencias": 4.7, "literatura": 4.6, "arte": 4.3}

mejor_de_cada_curso(estudiante1,estudiante2,estudiante3,estudiante4,estudiante5)"""