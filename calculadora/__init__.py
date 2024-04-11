def goleador(lista_jugadores):
    """
    La función goleador toma como entrada una lista de tuplas, donde cada tupla contiene el nombre, la cantidad de goles marcados, salvadas y asistencias por jugador.
    La función devuelve el nombre y número de goles marcados por el jugador que mas goles ha marcado.
    
    :param lista_jugadores: Almacena la lista de jugadores
    :return: El nombre y el número de goles.
    :doc-autor: Silva Julian
    """
    maxGol= -1
    for goleador in lista_jugadores:
        if(goleador[1]>maxGol):
            maxGol= goleador[1]
            maxNom= goleador[0]
    return maxNom, maxGol

def masInfluyente(lista_jugadores):
    """
    La función masInfluyente toma como entrada una lista de tuplas. Cada tupla contiene el nombre, goles marcados, salvadas y asistencias por jugador. 
    La función devuelve el nombre del jugador con más influencia en su equipo.
    
    :param lista_jugadores: Almacena la lista de jugadores
    :return: El nombre del jugador con la puntuación más alta
    :doc-autor: Silva Julian
    """
    estadisticas= map(lambda jug: jug[1]*1.5 + jug[2]*1.25 + jug[3], lista_jugadores)
    estadisticas= list(estadisticas)

    maxInf= max(estadisticas)
    indiceMax= estadisticas.index(maxInf)

    return lista_jugadores[indiceMax][0]