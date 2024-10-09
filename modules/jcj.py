import os, json
from modules import menuP as mP
from getpass import *
def JcJ():
        with open("modules/data/jvj.json", "r") as file: # Se carga la data del archivo json
            jvj = json.load(file)
        
        opc = ["PIEDRA","PAPEL","TIJERAS"]
        cntdr_jcj = {
            'rnds_gu_u' : 0,
            'rnds_gu_d' : 0
        }
        print("Antes de comenzar, es necesario registrarse.")
        rgstr_userU = input("Ingrese el nombre del jugador 1: ").upper()
        rgstr_userD = input("Ingrese el nombre del jugador 2: ").upper()

        if rgstr_userD == rgstr_userU: return input('No se puede registrar el mismo usuario')

        if rgstr_userU not in jvj: # Verificamos si no existe un usuario con ese nombre registrado
            print(f"Usuario {rgstr_userU} registrado con éxito\n")
            jvj.update({rgstr_userU : { # Creamos un campo en la data del archivo cuya clave sera el nombre que el usuario ingrese en la terminal, y su valor un diccionario
                "victorias": 0, # Iniciamos sus victorias en 0
                "derrotas": 0, # Iniciamos las derrotas en 0
                "historial": [{ # Iniciamos el historial con los datos de la partida actual
                    rgstr_userU: 0,
                    rgstr_userD: 0
                }] # Creamos su historial de partidas como un arreglo que contendra objetos con los datos de cada partida
            }})
        else: # Si ya existe entonces tomamos sus datos y creamos una nueva partida en el historial
            input(f'El usuario {rgstr_userU} ya existe en el sistema, se precargaran sus datos\n')
            jvj[rgstr_userU]["historial"].append({ # Actualizamos el historial agregandole un objeto de la partida actual
                # puntos en cero
                rgstr_userU: 0,
                rgstr_userD: 0
            })
        
        if rgstr_userD not in jvj:
            print(f"Usuario {rgstr_userD} registrado con éxito\n")
            jvj.update({rgstr_userD : { # Creamos un campo en la data del archivo cuya clave sera el nombre que el usuario ingrese en la terminal, y su valor un diccionario
                "victorias": 0, # Iniciamos sus victorias en 0
                "derrotas": 0, # Iniciamos las derrotas en 0
                "historial": [{ # Iniciamos el historial con los datos de la partida actual
                    rgstr_userD: 0,
                    rgstr_userU: 0
                }] # Creamos su historial de partidas como un arreglo que contendra objetos con los datos de cada partida
            }})
        else: # Si ya existe entonces tomamos sus datos y creamos una nueva partida en el historial
            input(f'El usuario {rgstr_userD} ya existe en el sistema, se precargaran sus datos\n')
            jvj[rgstr_userD]["historial"].append({ # Actualizamos el historial agregandole un objeto de la partida actual
                # puntos en cero
                rgstr_userD: 0,
                rgstr_userU: 0
            })

        current_round_historyUserU = jvj[rgstr_userU]["historial"][-1] # Variable para facilitar el acceso al historial de la partida actual del playerUno
        current_rount_historyUserD  = jvj[rgstr_userD]["historial"][-1]  # Variable para facilitar el acceso al historial de la partida actual del playerDos

        input("Usuarios registrados con éxito. Presiona Enter para continuar --> ")
        os.system('clear')
        vicConsUserUno = 0
        vicConsUserDos = 0
        while True:
            if current_round_historyUserU[rgstr_userU] < 3 and current_rount_historyUserD[rgstr_userD] < 3:
                user_u = getpass(f"---------------------------------\n{rgstr_userU} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                user_d = getpass(f"---------------------------------\n{rgstr_userD} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                print(user_u)
                print(user_d)
                if user_u == "PIEDRA" and user_d == "TIJERAS":
                    if vicConsUserDos >= 2: 
                        print(f"¡{rgstr_userD} tenía un escudo activo! {rgstr_userU} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    current_round_historyUserU[rgstr_userU] += 1
                    current_rount_historyUserD[rgstr_userU] += 1
                    print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_u == "PAPEL" and user_d == "PIEDRA":
                    if vicConsUserDos >= 2: 
                        print(f"¡{rgstr_userD} tenía un escudo activo! {rgstr_userU} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    current_round_historyUserU[rgstr_userU] += 1
                    current_rount_historyUserD[rgstr_userU] += 1
                    print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_u == "TIJERAS" and user_d == "PAPEL":
                    if vicConsUserDos >= 2: 
                        print(f"¡{rgstr_userD} tenía un escudo activo! {rgstr_userU} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    current_round_historyUserU[rgstr_userU] += 1
                    current_rount_historyUserD[rgstr_userU] += 1
                    print(f"¡{user_u} corta {user_d}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_d == "PIEDRA" and user_u == "TIJERAS":
                    if vicConsUserUno >= 2: 
                        print(f"{rgstr_userU} tenía un escudo activo! Aunque {rgstr_userD} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    current_round_historyUserU[rgstr_userD] += 1
                    current_rount_historyUserD[rgstr_userD] += 1
                    print(f"¡{user_d} aplasta {user_u}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_d == "PAPEL" and user_u == "PIEDRA":
                    if vicConsUserUno >= 2: 
                        print(f"{rgstr_userU} tenía un escudo activo! Aunque {rgstr_userD} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    current_round_historyUserU[rgstr_userD] += 1
                    current_rount_historyUserD[rgstr_userD] += 1
                    print(f"¡{user_d} envuelve {user_u}! {rgstr_userU} has perdido esta vez.\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_d == "TIJERAS" and user_u == "PAPEL":
                    if vicConsUserUno >= 2: 
                        print(f"{rgstr_userU} tenía un escudo activo! Aunque {rgstr_userD} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    current_round_historyUserU[rgstr_userD] += 1
                    current_rount_historyUserD[rgstr_userD] += 1
                    print(f"¡{user_d} corta {user_u}! No te preocupes {rgstr_userU} , ¡a la siguiente lo conseguirás!\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_u == user_d:
                    print(f"¡Empate! Ambos eligieron lo mismo. ¡Parece que están en sintonía! ¿Van de nuevo?\nMARCADOR: {current_round_historyUserU[rgstr_userU]} - {current_rount_historyUserD[rgstr_userD]}")
                elif user_u not in opc or user_d not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                if current_round_historyUserU[rgstr_userU] > current_rount_historyUserD[rgstr_userD]:
                    current_round_historyUserU["ganador"] = rgstr_userU
                    current_rount_historyUserD["ganador"] = rgstr_userU
                    jvj[rgstr_userD]["derrotas"] += 1
                    jvj[rgstr_userU]["victorias"] += 1
                    input(f"{rgstr_userU} es el ganador")
                else:
                    current_round_historyUserU["ganador"] = rgstr_userD
                    current_rount_historyUserD["ganador"] = rgstr_userD
                    jvj[rgstr_userD]["victorias"] += 1
                    jvj[rgstr_userU]["derrotas"] += 1
                    input(f"{rgstr_userD} es el ganador")
                
                with open("modules/data/jvj.json", "w") as file:
                    json.dump(jvj, file, indent=4)

                os.system('cls')
                break