def goleador(lista_jugadores):
    """
    La función goleador toma como entrada una lista de tuplas, donde cada tupla contiene el nombre, la cantidad de goles marcados, salvadas y asistencias por jugador.
    La función devuelve el nombre y número de goles marcados por el jugador que mas goles ha marcado.
    
    :param lista_jugadores: Almacena la lista de jugadores
    :return: El nombre y el número de goles.
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
    """
    estadisticas= map(lambda jug: jug[1]*1.5 + jug[2]*1.25 + jug[3], lista_jugadores)
    estadisticas= list(estadisticas)

    maxInf= max(estadisticas)
    indiceMax= estadisticas.index(maxInf)

    return lista_jugadores[indiceMax][0]

def promGoles(lista_jugadores):
    """
    La función promGoles toma como entrada una lista de tuplas. Cada tupla contiene el nombre, goles marcados, salvadas y asistencias por jugador.
    La función devuelve el promedio de goles marcados por el equipo.
    
    :param lista_jugadores: Almacena la lista de jugadores
    :return: El promedio de goles marcados
    """
    partidos= 25
    suma= sum(map(lambda jug: jug[1], lista_jugadores))
    return suma/partidos

def promedioGoleador(jugador_est):
    """
    La función promedioGoleador toma como entrada una tupla que contiene nombre y goles de un jugador.
    La función devuelve el promedio de goles del goleador
    
    :param jugador_est: Almacena la tupla del jugador
    :return: El promedio de goles por partido
    """
    partidos= 25
    return jugador_est[0]/25