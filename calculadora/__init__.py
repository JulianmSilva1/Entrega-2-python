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