def mejor_del_salon(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:dict,estudiante5:dict)->str:
    #i=0
    
    mejor_promedio = (estudiante1["matematicas"]+estudiante1["español"]+estudiante1["ciencias"]+estudiante1["literatura"]+estudiante1["arte"])/5
    estu = estudiante1["nombre"].lower()
    #print(mejor_promedio)
    if mejor_promedio<(estudiante2["matematicas"]+estudiante2["español"]+estudiante2["ciencias"]+estudiante2["literatura"]+estudiante2["arte"])/5:
        mejor_promedio=(estudiante2["matematicas"]+estudiante2["español"]+estudiante2["ciencias"]+estudiante2["literatura"]+estudiante2["arte"])/5
        #print(mejor_promedio)
        estu = estudiante2["nombre"].lower()
    else:    
        if mejor_promedio==(estudiante2["matematicas"]+estudiante2["español"]+estudiante2["ciencias"]+estudiante2["literatura"]+estudiante2["arte"])/5:
            if estudiante1["nombre"]<estudiante2["nombre"].lower():
                estu = estudiante1["nombre"].lower()
            else:
                estu = estudiante2["nombre"].lower()
        #print(mejor_promedio)
    if mejor_promedio<(estudiante3["matematicas"]+estudiante3["español"]+estudiante3["ciencias"]+estudiante3["literatura"]+estudiante3["arte"])/5:
        mejor_promedio=(estudiante3["matematicas"]+estudiante3["español"]+estudiante3["ciencias"]+estudiante3["literatura"]+estudiante3["arte"])/5
        estu = estudiante3["nombre"].lower()
    else:
        if mejor_promedio==(estudiante3["matematicas"]+estudiante3["español"]+estudiante3["ciencias"]+estudiante3["literatura"]+estudiante3["arte"])/5:
            if estu<estudiante3["nombre"].lower():
                estu = estu.lower()
            else:
                estu = estudiante3["nombre"].lower()
    if mejor_promedio<(estudiante4["matematicas"]+estudiante4["español"]+estudiante4["ciencias"]+estudiante4["literatura"]+estudiante4["arte"])/5:
        mejor_promedio=(estudiante4["matematicas"]+estudiante4["español"]+estudiante4["ciencias"]+estudiante4["literatura"]+estudiante4["arte"])/5
        estu = estudiante4["nombre"].lower()
    else:
        if mejor_promedio==(estudiante4["matematicas"]+estudiante4["español"]+estudiante4["ciencias"]+estudiante4["literatura"]+estudiante4["arte"])/5:
            if estu<estudiante4["nombre"].lower():
                estu = estu.lower()
            else:
                estu = estudiante4["nombre"].lower()
    if mejor_promedio<(estudiante5["matematicas"]+estudiante5["español"]+estudiante5["ciencias"]+estudiante5["literatura"]+estudiante5["arte"])/5:
        mejor_promedio=(estudiante5["matematicas"]+estudiante5["español"]+estudiante5["ciencias"]+estudiante5["literatura"]+estudiante5["arte"])/5
        estu = estudiante5["nombre"].lower()
    else:
        if mejor_promedio==(estudiante5["matematicas"]+estudiante5["español"]+estudiante5["ciencias"]+estudiante5["literatura"]+estudiante5["arte"])/5:
            if estu<estudiante5["nombre"].lower():
                estu = estu.lower()
            else:
                estu = estudiante5["nombre"].lower()

    return estu


estudiante1 = {"nombre": "juan", "matematicas": 3.4, "español": 5.0, "ciencias": 2.9, "literatura": 4.2, "arte": 3.2}
estudiante2 = {"nombre": "andres", "matematicas": 2.1, "español": 5.0, "ciencias": 3.0, "literatura": 4.1, "arte": 3.5}
estudiante3 = {"nombre": "camilo", "matematicas": 5.0, "español": 4.2, "ciencias": 4.4, "literatura": 3.5, "arte": 4.7}
estudiante4 = {"nombre": "Danilo", "matematicas": 3.2, "español": 3.7, "ciencias": 3.1, "literatura": 4.7, "arte": 3.4}
estudiante5 = {"nombre": "Pedro", "matematicas": 5.0, "español": 4.2, "ciencias": 4.4, "literatura": 3.5, "arte": 4.7}

print(mejor_del_salon(estudiante1,estudiante2,estudiante3,estudiante4,estudiante5))
