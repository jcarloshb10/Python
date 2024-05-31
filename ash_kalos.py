"""Ash Ketchum, el personaje principal del anime Pokémon, está a punto de luchar en la final de la liga Kalos. En estos eventos compiten los mejores entrenadores del mundo en batallas donde cada entrenador puede tener 3, 4, 5 o 6 criaturas. Ash quiere saber, para una cantidad de criaturas específica, si él podrá formar un equipo únicamente con Pokémon seudolegendarios para competir en la final. Un pokemon seudolegendario es aquel que en la suma de sus estadísticas de combate tiene 600 puntos o más.
Las estadísticas de combate de cada pokemon son 6:  
"ataque"
"defensa"
"ataque_especial"
"defensa_especial"
"velocidad"
"vida"  
Escriba una función que, dada una lista de diccionarios (cada uno representando un pokémon) con las anteriores estadísticas, determine si Ash podrá formar un equipo de pokémon seudolegendarios para afrontar la final de la liga. En caso que Ash pueda formar un equipo, retorne una lista con los nombres de las criaturas que Ash utilizaría en la batalla. Si es imposible generar un equipo que cumpla con las condiciones, retorne None."""

def construir_equipo_pokemon(cantidad:int,lista_pkmn:list)->list:
    lista = []
    if lista_pkmn.__len__()<3:
        return None
    for i in lista_pkmn:
        if i["vida"]+i["ataque"]+i["defensa"]+i["ataque_especial"]+i["defensa_especial"]+i["velocidad"]>=600:
            lista.append(i["nombre"])
    if lista.__len__()<3 or lista.__len__()!=cantidad:
        return None

    return  lista




"""lista_pkmn = [{'nombre': 'Rayquaza', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Arceus', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Solgaleo', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 200, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Charizard-X', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 50, 'defensa_especial': 50, 'velocidad': 100}, {'nombre': 'Greninja', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Swellow', 'vida': 60, 'ataque': 80, 'defensa': 50, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 150}, {'nombre': 'Pikachu', 'vida': 20, 'ataque': 20, 'defensa': 20, 'ataque_especial': 20, 'defensa_especial': 20, 'velocidad': 20}]
cantidad = 4"""

"""cantidad = 5
lista_pkmn = [{'nombre': 'Rayquaza', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Pikachu', 'vida': 100, 'ataque': 1001, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 1, 'velocidad': 1}]
"""
cantidad = 4
lista_pkmn = [{'nombre': 'Greninja', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Talonflame', 'vida': 50, 'ataque': 90, 'defensa': 40, 'ataque_especial': 60, 'defensa_especial': 40, 'velocidad': 90}, {'nombre': 'Sceptile', 'vida': 100, 'ataque': 90, 'defensa': 80, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 80}, {'nombre': 'Swellow', 'vida': 60, 'ataque': 80, 'defensa': 50, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 150}, {'nombre': 'Pikachu', 'vida': 20, 'ataque': 20, 'defensa': 20, 'ataque_especial': 20, 'defensa_especial': 20, 'velocidad': 20}]

print(construir_equipo_pokemon(cantidad,lista_pkmn))