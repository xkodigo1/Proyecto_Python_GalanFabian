import os, json, random, platform
from modules import menuP as mP
def JvE():
        
        # Abrimos el archivo JSON que contiene los datos del modo JvE
        with open("modules/data/jve.json", "r") as file:
            jve = json.load(file) # Cargamos los datos del archivo en la variable 'jve'

        opc = ["PIEDRA","PAPEL","TIJERAS"]
        
        print("Antes de comenzar, es necesario registrarse.")
        rgstr_user = input("Ingrese su nombre de usuario: ").upper().strip()

        if rgstr_user not in jve: # Verificamos si no existe un usuario con ese nombre registrado
            input("Usuario registrado con éxito. Presiona Enter para continuar --> ")
            jve.update({rgstr_user : { # Creamos un campo en la data del archivo cuya clave sera el nombre que el usuario ingrese en la terminal, y su valor un diccionario
                "victorias": 0, # Iniciamos sus victorias en 0
                "derrotas": 0, # Iniciamos las derrotas en 0
                "historial": [{ # Iniciamos el historial con los datos de la partida actual
                    "puntos_favor": 0,
                    "puntos_contrincante": 0
                }] # Creamos su historial de partidas como un arreglo que contendra objetos con los datos de cada partida
            }})
        else: # Si ya existe entonces tomamos sus datos y creamos una nueva partida en el historial
            input('El usuario ya existe en el sistema, se precargaran sus datos')
            jve[rgstr_user]["historial"].append({ # Actualizamos el historial agregandole un objeto de la partida actual
                # puntos en cero
                "puntos_favor": 0,
                "puntos_contrincante": 0
            })
        
        jve["environment"]["historial"].append({ # Creamos un nuevo objeto en el historial del env que representara la partida actual
            "puntos_favor": 0,
            "puntos_contrincante": 0
        })
        
        os.system("cls" if platform.system() == "Windows" else "clear")

        current_round_historyUser = jve[rgstr_user]["historial"][-1] # Variable para facilitar el acceso al historial de la partida actual
        current_rount_historyEnv  = jve["environment"]["historial"][-1]  # Variable para facilitar el acceso al historial de la partida actual
        
        vicConsUser = 0
        vicConsEnv = 0
        while True:
            if current_round_historyUser['puntos_favor'] < 3 and current_rount_historyEnv['puntos_favor'] < 3:
                env = random.choice(opc)
                user = input("---------------------------------\nElige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                if user == "PIEDRA" and env == "TIJERAS":
                    if vicConsEnv >= 2: 
                        print("¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    current_round_historyUser["puntos_favor"] += 1
                    current_rount_historyEnv["puntos_contrincante"] += 1
                    print(f"¡{user} aplasta {env}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif user == "PAPEL" and env == "PIEDRA":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    current_round_historyUser['puntos_favor'] += 1
                    current_rount_historyEnv["puntos_contrincante"] += 1
                    print(f"¡{user} envuelve {env}! ¡Muy bien, esta vez ganaste tú!\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif user == "TIJERAS" and env == "PAPEL":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    current_round_historyUser['puntos_favor'] += 1
                    current_rount_historyEnv["puntos_contrincante"] += 1
                    print(f"¡{user} corta {env}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif env == "PIEDRA" and user == "TIJERAS":
                    if vicConsUser >= 2: 
                        print(f"{rgstr_user} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    current_rount_historyEnv['puntos_favor'] += 1
                    current_round_historyUser["puntos_contrincante"] += 1
                    print(f"¡{env} aplasta {user}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif env == "PAPEL" and user == "PIEDRA":
                    if vicConsUser >= 2: 
                        print(f"{rgstr_user} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    current_rount_historyEnv['puntos_favor'] += 1
                    current_round_historyUser["puntos_contrincante"] += 1
                    print(f"¡{env} envuelve {user}! Has perdido esta vez.\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif env == "TIJERAS" and user == "PAPEL":
                    if vicConsUser >= 2: 
                        print(f"{rgstr_user} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    current_rount_historyEnv['puntos_favor'] += 1
                    current_round_historyUser["puntos_contrincante"] += 1
                    print(f"¡{env} corta {user}! No te preocupes, ¡a la siguiente lo conseguirás!\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                elif user == env:
                    print(f"¡Empate! Ambos elegimos lo mismo. ¡Parece que estamos en sintonía! ¿Vamos de nuevo?\nMARCADOR: {current_round_historyUser['puntos_favor']} - {current_rount_historyEnv['puntos_favor']}")
                    vicConsEnv = 0
                    vicConsUser = 0
                elif user not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                if current_round_historyUser['puntos_favor'] > current_rount_historyEnv['puntos_favor']:
                    current_round_historyUser.update({"ganador": rgstr_user})
                    current_rount_historyEnv.update({"ganador": rgstr_user})
                    jve[rgstr_user]["victorias"] += 1
                    jve["environment"]["derrotas"] += 1
                    input(f"{rgstr_user} es el ganador")
                else: 
                    current_round_historyUser.update({"ganador": "environment"})
                    current_rount_historyEnv.update({"ganador": "environment"})
                    jve[rgstr_user]["derrotas"] += 1
                    jve["environment"]["victorias"] += 1
                    input("Entorno es el ganador")

                with open("modules/data/jve.json", "w") as file:
                    json.dump(jve, file, indent=4)
                    file.close()

                os.system('clear')
                break