import os, json, platform

def estadisticas():
    print("\nEstadísticas de los modos JvE & JvJ:")

    with open("modules/data/jvj.json", "r") as file:
        jvj = json.load(file)

    input("Tres mejores jugadores del modo JvJ son:\n ")
    items_list = list(jvj.items())
    if len(items_list):
        for i in range(len(items_list)):
            for j in range(0, len(items_list)-i-1):
                # Comparar las victorias de los elementos adyacentes
                if items_list[j][1]['victorias'] < items_list[j + 1][1]['victorias']:
                    # Intercambiar los elementos si están en el orden incorrecto
                    items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]

        data_ordenada = dict(items_list)  

        contador = 0
        for key in data_ordenada:
            if contador == 3: break
            print(f"{contador + 1}. {key} con {data_ordenada[key]['victorias']} victorias")
            contador += 1
        
        input(f"\njugador que ocupa el ultimo puesto del ranking es {list(data_ordenada)[-1]} con {data_ordenada[list(data_ordenada)[-1]]['victorias']} victorias\n")
    else: input("No hay jugadores registrados en el modo JvJ, por lo que no hay estadisticas de este modo\n")

    input("Promedio de jugadores")

    with open("modules/data/jve.json", "r") as file:
        data = json.load(file)

    derrotas_contra_environment = {}
# Recorrer los jugadores y sus historiales
    for jugador, datos in data.items():
        # Contador de derrotas contra "environment"
        derrotas = 0
        for partida in datos["historial"]:
            # Si el ganador es "environment" y el jugador actual es el contrincante
            if partida["ganador"] == "environment" and jugador != "environment":
                derrotas += 1
        # Si el jugador tiene derrotas contra "environment", almacenarlas
        if derrotas > 0:
            derrotas_contra_environment[jugador] = derrotas

    # Encontrar el máximo de derrotas
    if derrotas_contra_environment:
        max_derrotas = max(derrotas_contra_environment.values())
        # Listar los jugadores con el máximo de derrotas
        jugadores_max_derrotas = [jugador for jugador, derrotas in derrotas_contra_environment.items() if derrotas == max_derrotas]

        # Mostrar los resultados
        print(f"Jugadores con más derrotas contra environment: {jugadores_max_derrotas[0]}, con {max_derrotas} derrotas.")
    else:
        print("Ningún jugador ha perdido contra environment.\n")

    input("Promedio de jugadores que le han ganado a la IA")

    ganadores_contra_environment = set()

# Contar cuántos jugadores han vencido al menos una vez a "environment"
    for jugador, datos in data.items():
        for partida in datos["historial"]:
            # Si el jugador actual ha ganado la partida y el oponente era "environment"
            if partida["ganador"] == jugador and jugador != "environment":
                ganadores_contra_environment.add(jugador)

    # Calcular el promedio de jugadores que le han ganado a "environment"
    total_ganadores = len(ganadores_contra_environment)
    total_partidas = sum(len(datos["historial"]) for jugador, datos in data.items())

    # Calcular el promedio
    promedio_ganadores = total_ganadores / total_partidas if total_partidas > 0 else 0

    # Mostrar resultados
    print(f"Total de jugadores que le han ganado a 'environment': {total_ganadores}")
    print(f"Promedio de jugadores que le han ganado a 'environment' en relación a las partidas jugadas: {promedio_ganadores:.2f}")



    return input()