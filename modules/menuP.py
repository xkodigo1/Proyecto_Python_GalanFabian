import os
import random
import modules as pack
cntdr_pve = {
    'pts_env':0,
    'pts_user':0,
    'rnds_gu':0,
    'rnds_ge':0,
    'rslt':0
}
cntdr_jcj = {
    'rnds_gu_u' : 0,
    'rnds_gu_d' : 0
}
opc = ["PIEDRA","PAPEL","TIJERAS"]
def menuP():
    print(pack.ttl_menuP)
    input("¡Bienvenido a Rock, Paper N' Scissors! ¿Preparado para poner a prueba tu suerte mediante una elecciòn?\nPresiona Enter para continuar --> ")
    os.system("clear")
    opc_user = int(input("Es hora de elegir còmo quieres jugar. Elige una opcion:\n1). PvE (Jugador vs Entorno)\n2). JcJ (Jugador contra Jugador)\n--> "))
    os.system("clear")
    if opc_user == 1:
        print("Antes de comenzar, es necesario registrarse.")
        rgstr_user = input("Ingrese su nombre de usuario: ")
        users = {
            'name' : rgstr_user
        }
        input("Usuario registrado con éxito. Presiona Enter para continuar --> ")
        os.system("clear")
        vicConsUser = 0
        vicConsEnv = 0
        while True:
            if cntdr_pve['rnds_gu'] < 3 and cntdr_pve['rnds_ge'] < 3:
                opc = ["PIEDRA","PAPEL","TIJERAS"]
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
                    print(f"¡Empate! Ambos elegimos lo mismo. ¡Parece que están en sintonía! ¿Vamos de nuevo?\nMARCADOR: {cntdr_pve['rnds_gu']} - {cntdr_pve['rnds_ge']}")
                elif user not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                print(f"{users['name']} es el ganador" if cntdr_pve['rnds_gu'] > cntdr_pve['rnds_ge'] else "Entorno es el ganador")
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
        input("Usuarios registrados con éxito. Presiona Enter para continuar --> ")
        os.system('clear')
        vicConsUserUno = 0
        vicConsUserDos = 0
        while True:
            if cntdr_jcj['rnds_gu_u'] < 3 and cntdr_jcj['rnds_gu_d'] < 3:
                user_u = input(f"---------------------------------\n{users['nameU']} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                user_d = input(f"---------------------------------\n{users['nameD']} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
                if user_u == "PIEDRA" and user_d == "TIJERAS":
                    if vicConsUserDos >= 2: 
                        print(f"¡{users['nameD']} tenía un escudo activo! {users['nameU']} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    cntdr_jcj['rnds_gu_u'] += 1
                    print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_u == "PAPEL" and user_d == "PIEDRA":
                    if vicConsUserDos >= 2: 
                        print(f"¡{users['nameD']} tenía un escudo activo! {users['nameU']} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    cntdr_jcj['rnds_gu_u'] += 1
                    print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_u == "TIJERAS" and user_d == "PAPEL":
                    if vicConsUserDos >= 2: 
                        print(f"¡{users['nameD']} tenía un escudo activo! {users['nameU']} aunque ganaste esta ronda, no obtienes puntos.")
                        vicConsUserDos = 0
                        vicConsUserUno += 1
                        continue
                    vicConsUserUno += 1
                    cntdr_jcj['rnds_gu_u'] += 1
                    print(f"¡{user_u} corta {user_d}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_d == "PIEDRA" and user_u == "TIJERAS":
                    if vicConsUserUno >= 2: 
                        print(f"{users['nameU']} tenía un escudo activo! Aunque {users['nameD']} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    cntdr_jcj['rnds_gu_d'] += 1
                    print(f"¡{user_d} aplasta {user_u}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_d == "PAPEL" and user_u == "PIEDRA":
                    if vicConsUserUno >= 2: 
                        print(f"{users['nameU']} tenía un escudo activo! Aunque {users['nameD']} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    cntdr_jcj['rnds_gu_d'] += 1
                    print(f"¡{user_d} envuelve {user_u}! {users['nameU']} has perdido esta vez.\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_d == "TIJERAS" and user_u == "PAPEL":
                    if vicConsUserUno >= 2: 
                        print(f"{users['nameU']} tenía un escudo activo! Aunque {users['nameD']} ganó esta ronda, no obtendra puntos.")
                        vicConsUserUno = 0
                        vicConsUserDos += 1
                        continue
                    vicConsUserDos += 1
                    cntdr_jcj['rnds_gu_d'] += 1
                    print(f"¡{user_d} corta {user_u}! No te preocupes {users['nameU']} , ¡a la siguiente lo conseguirás!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_u == user_d:
                    print(f"¡Empate! Ambos eligieron lo mismo. ¡Parece que están en sintonía! ¿Van de nuevo?\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
                elif user_u not in opc or user_d not in opc:
                    input("Elección no válida. Presiona Enter para regresar --> ")
            else: 
                print(f"{users['nameU']} es el ganador" if cntdr_jcj['rnds_gu_u'] > cntdr_jcj['rnds_gu_d'] else f"{users['nameD']} es el ganador")
                break

