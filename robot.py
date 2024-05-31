"""Usted quiere anticipar el movimiento del nuevo robot que recibió como regalo de cumpleaños. El robot tiene una brújula interna que le permite saber hacia qué punto cardinal está mirando actualmente: Norte, Sur, Este, u Oeste. Además, el robot tiene un control remoto que permite girarlo hacia la izquierda o la derecha, y también pedirle que dé media vuelta. Usted debe escribir una función que, dados 3 comandos que se envíen usando el control remoto, calcule la orientación final del robot.

Nota: La representación de los puntos cardinales que llegan por parámetro es la siguiente:

"N", para Norte.

"S", para Sur.

"E", para Este.

"W", para Oeste.

Las representaciones de los comandos del control remoto que llegan por parámetro son las siguientes:

"L", para girar a la izquierda.

"R", para girar a la derecha.

"H", para dar media vuelta.

".", para mantener la orientación actual."""

def movimiento_robot(orientacion_actual:str,giro_1:str,giro_2:str,giro_3:str)->str:
    cont = 1
    while cont<=3:
        
        if cont==1:
            x=giro_1
        elif cont==2:
            x=giro_2
        else:
            x=giro_3

        if orientacion_actual=="N":
            if x=="L":
                orientacion_actual="W"
            elif x=="R":
                orientacion_actual="E"
            elif x=="H":
                orientacion_actual="S"
            else:
                orientacion_actual="N"
        elif orientacion_actual=="S":
            if x=="L":
                orientacion_actual="E"
            elif x=="R":
                orientacion_actual="W"
            elif x=="H":
                orientacion_actual="N"
            else:
                orientacion_actual="S"
        elif orientacion_actual=="E":
            if x=="L":
                orientacion_actual="N"
            elif x=="R":
                orientacion_actual="S"
            elif x=="H":
                orientacion_actual="W"
            else:
                orientacion_actual="E"
        elif orientacion_actual=="W":
            if x=="L":
                orientacion_actual="S"
            elif x=="R":
                orientacion_actual="N"
            elif x=="H":
                orientacion_actual="E"
            else:
                orientacion_actual="W"
        cont=cont+1        
    return orientacion_actual            