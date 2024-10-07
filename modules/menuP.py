import os
import random
import modules as pack
cntdr = {
    'pts_env':0,
    'pts_user':0,
    'rnds_gu':0,
    'rnds_ge':0,
    'rslt':0
}

def menuP():
    print(pack.ttl_menuP)
    input("¡Bienvenido a Rock, Paper N' Scissors! ¿Preparado para poner a prueba tu suerte mediante una elecciòn?\nPresiona Enter para continuar --> ")
    os.system("cls")
    opc_user = int(input("Es hora de elegir còmo quieres jugar. Elige una opcion:\n1). PvE (Jugador vs Entorno)\n2). JcJ (Jugador contra Jugador)\n--> "))
    os.system("cls")
    if opc_user == 1:
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
            if cntdr["rnds_gu"] < 3 and cntdr["rnds_ge"] < 3:
                opc = ["PIEDRA","PAPEL","TIJERAS"]
                env = random.choice(opc)
                print(env)
                user = input("---------------------------------\nElige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                if user == "PIEDRA" and env == "TIJERAS":
                    if vicConsEnv >= 2: 
                        print("¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr["rnds_gu"] += 1
                    print(f"¡{user} aplasta {env}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif user == "PAPEL" and env == "PIEDRA":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr["rnds_gu"] += 1
                    print(f"¡{user} envuelve {env}! ¡Muy bien, esta vez ganaste tú!\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif user == "TIJERAS" and env == "PAPEL":
                    if vicConsEnv >= 2: 
                        print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsEnv = 0
                        vicConsUser += 1
                        continue
                    vicConsUser += 1
                    cntdr["rnds_gu"] += 1
                    print(f"¡{user} corta {env}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif env == "PIEDRA" and user == "TIJERAS":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr["rnds_ge"] += 1
                    print(f"¡{env} aplasta {user}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif env == "PAPEL" and user == "PIEDRA":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr["rnds_ge"] += 1
                    print(f"¡{env} envuelve {user}! Has perdido esta vez.\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif env == "TIJERAS" and user == "PAPEL":
                    if vicConsUser >= 2: 
                        print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
                        vicConsUser = 0
                        vicConsEnv += 1
                        continue
                    vicConsEnv += 1
                    cntdr["rnds_ge"] += 1
                    print(f"¡{env} corta {user}! No te preocupes, ¡a la siguiente lo conseguirás!\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif user == env:
                    print(f"¡Empate! Ambos elegimos lo mismo. ¡Parece que están en sintonía! ¿Vamos de nuevo?\nMARCADOR: {cntdr["rnds_gu"]} - {cntdr["rnds_ge"]}")
                elif user not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                print(f"{users["name"]} es el ganador" if cntdr["rnds_gu"] > cntdr["rnds_ge"] else "Entorno es el ganador")
                break
            #input("Presiona Enter para regresar --> ")
            #retry = input("¿Desea jugar de nuevo? (Sí = Y / No = N): ").upper()
            #if retry != "Y":
            #    print("Gracias por jugar. ¡Hasta la próxima!")
            #    break
            #else:
            #        print("¡Vamos a jugar otra partida!")
            #        continue
                
    
    if opc_user == 2:
        print("Antes de comenzar, es necesario registrarse.")
        rgstr_userU = input("Ingrese el nombre del jugador 1: ")
        rgstr_userD = input("Ingrese el nombre del jugador 2: ")
        users = {
            'nameU' : rgstr_userU,
            'nameD' : rgstr_userD
        }
        input("Usuario registrado con éxito. Presiona Enter para continuar --> ")
        