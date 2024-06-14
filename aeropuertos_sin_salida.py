def listar_aeropuertos_sin_salida(vuelos: dict) -> list:
    aeropuertos_salida = set()  # Conjunto de aeropuertos de salida
    aeropuertos_llegada = set()  # Conjunto de aeropuertos de llegada
    
    # Obtener los aeropuertos de salida y llegada
    for vuelo, info_vuelo in vuelos.items():
        aeropuertos_salida.add(info_vuelo['origen'])
        aeropuertos_llegada.add(info_vuelo['destino'])
    
    # Identificar los aeropuertos a los que llegaron vuelos pero no hubo salidas
    aeropuertos_sin_salida = aeropuertos_llegada - aeropuertos_salida
    
    return list(aeropuertos_sin_salida)

# Ejemplo de uso
vuelos = {
    'Vuelo1': {'aerolínea': 'Aerolínea1', 'origen': 'AER1', 'destino': 'AER2'},
    'Vuelo2': {'aerolínea': 'Aerolínea2', 'origen': 'AER2', 'destino': 'AER3'},
    'Vuelo3': {'aerolínea': 'Aerolínea3', 'origen': 'AER3', 'destino': 'AER6'}
}

print(listar_aeropuertos_sin_salida(vuelos))  # Salida esperada: ['AER3']