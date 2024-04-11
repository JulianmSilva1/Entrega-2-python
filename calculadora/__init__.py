def goleador(lista_jugadores):
    """
    La función goleador toma como entrada una lista de tuplas, donde cada tupla contiene el nombre, la cantidad de goles marcados, salvadas y asistencias por un jugador.
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