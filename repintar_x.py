""" 
Un matemático ha diseñado un juego muy sencillo para que sus hijos practiquen operaciones aritméticas básicas. En este juego, él les da una matriz cuadrada de más de 3x3 y les pide que "repinten la X" usando una operación determinada. Es decir, ellos tienen que devolver la matriz aplicando la operación sobre todas las casillas que hacen parte de las diagonales de la matriz.
Las operaciones posibles son sumar, restar, multiplicar y dividir el valor de cada casilla por él mismo. Por ejemplo, si en una casilla de la X el número original era 5 y la operación que se debe aplicar es la suma, el valor 5 deberá reemplazarse por 10. 
Construya una función que le sirva a los hijos del matemático para verificar sus respuestas. La función recibe una matriz cuadrada, una operación y retorna la matriz modificada según las reglas del juego.  
"""

def pintar_x(matriz:list,operacion:str)->list:
    lista = matriz.copy()
    operaciones = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
    }
    operacion = operaciones.get(operacion)
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if i == j or i + j == len(matriz) - 1:  
                resultado = operacion(matriz[i][j], matriz[i][j])
                lista[i][j] = resultado
    return lista
 
