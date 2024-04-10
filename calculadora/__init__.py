def listarjugadores(names, goles, salvadas, asistencias):
    """
    La función listarjugadores toma las listas de nombres, goles, salvadas y asistencias.
    y devuelve una lista de tuplas que contienen el nombre de cada jugador, los goles marcados, las salvadas realizadas y las asistencias.
    
    
    :param names: almacena los nombres de los jugadores
    :param goles: Almacena los goles de cada jugador
    :param salvadas: Almacena el número de salvaciones de cada jugador
    :param asistencias: Almacena el número de asistencias que ha realizado un jugador
    :return: Una lista de tuplas
    :doc-autor: Silva Julian
    """
    lista_jugadores= []
    for i in range(len(names)):
        lista_jugadores.append((names[i], goles[i], salvadas[i], asistencias[i]))
    return lista_jugadores

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