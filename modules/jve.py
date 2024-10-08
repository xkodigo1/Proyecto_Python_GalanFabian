import os
import random
from modules import menuP as mP
def JvE():
        opc = ["PIEDRA","PAPEL","TIJERAS"]
        cntdr_pve = {
            'pts_env':0,
            'pts_user':0,
            'rnds_gu':0,
            'rnds_ge':0,
            'rslt':0
        }
        print("Antes de comenzar, es necesario registrarse.")
        rgstr_user = input("Ingrese su nombre de usuario: ")
        users = {
            'name' : rgstr_user
        }
        input("Usuario registrado con éxito. Presiona Enter para continuar --> ")
        os.system("cls")
        vicConsUser = 0
        vicConsEnv = 0
        while True:
            if cntdr_pve['rnds_gu'] < 3 and cntdr_pve['rnds_ge'] < 3:
                env = random.choice(opc)
                user = input("---------------------------------\nElige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                if user == "PIEDRA" and env == "TIJERAS":
                    if vicConsEnv >= 2: 
                        print("¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr_pve['rnds_gu'] += 1
                    print(f"¡{user} aplasta {env}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif user == "PAPEL" and env == "PIEDRA":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr_pve['rnds_gu'] += 1
                    print(f"¡{user} envuelve {env}! ¡Muy bien, esta vez ganaste tú!\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif user == "TIJERAS" and env == "PAPEL":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr_pve['rnds_gu'] += 1
                    print(f"¡{user} corta {env}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif env == "PIEDRA" and user == "TIJERAS":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr_pve['rnds_ge'] += 1
                    print(f"¡{env} aplasta {user}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif env == "PAPEL" and user == "PIEDRA":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr_pve['rnds_ge'] += 1
                    print(f"¡{env} envuelve {user}! Has perdido esta vez.\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif env == "TIJERAS" and user == "PAPEL":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr_pve['rnds_ge'] += 1
                    print(f"¡{env} corta {user}! No te preocupes, ¡a la siguiente lo conseguirás!\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif user == env:
                    print(f"¡Empate! Ambos elegimos lo mismo. ¡Parece que estamos en sintonía! ¿Vamos de nuevo?\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                    vicConsEnv = 0
                    vicConsUser = 0
                elif user not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                cntdr_pve['rnds_gu'] = 0
                cntdr_pve['rnds_ge'] = 0
                print(f"{users['name']} es el ganador." if cntdr_pve['rnds_gu'] > cntdr_pve['rnds_ge'] else "Entorno es el ganador.")
                os.system('cls')
                break