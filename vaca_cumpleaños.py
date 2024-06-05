"""
Una clase de estudiantes ejemplares ha decidido hacer una vaca para el cumpleaños de su profesor favorito. Para esto, un estudiante recorrerá todo el salón recogiendo el dinero que cada estudiante va a aportar. Tienen dos opciones de regalo: una botella de licor que cuesta 120.000 o un pastel que cuesta 35.000. Además, el estudiante que más dinero ponga, será el que tenga el honor de darle el regalo al profesor. Recree este caso en una función que reciba una matriz que representa al salón y una cadena que indica el regalo. Debe retornar una lista cuya primera posición es un mensaje que indica si el dinero alcanzó para la vaca y las siguientes dos posiciones son las coordenadas del puesto del estudiante que más aportó.  
"""

def hacer_la_vaca(salon:list,vaca:str)->list:
    lista = []
    dinero = 0
    x = 0
    y = 0
    mayor_aporte = 0

    for i in range(0,len(salon)):
        for j in range(0,len(salon[0])):
            dinero += salon[i][j]
            if mayor_aporte < salon[i][j]:
                mayor_aporte = salon[i][j]
                x = i
                y = j

    if dinero>=35000 and vaca=="pastel":
        lista.append("Hay Vaca")
    elif vaca == "pastel" and dinero<35000:
        lista.append("No Alcanza")
    elif dinero>=120000 and vaca=="botella":
        lista.append("Hay Vaca")
    else:
        lista.append("No Alcanza")

    lista.append(x)
    lista.append(y)

    return lista

salon = [[1,2,3],[4,5,6],[7,8,9]]
vaca = "pastel"
print(len(salon))
print(hacer_la_vaca(salon,vaca))