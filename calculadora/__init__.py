def listarjugadores(names, goles, salvadas, asistencias):
    lista_jugadores= []
    for jugador in names:
        lista_jugadores.append((jugador, goles[0], salvadas[0], asistencias[0]))
    return lista_jugadores