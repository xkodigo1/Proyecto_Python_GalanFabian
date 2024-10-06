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
    opc_user = int(input("Es hora de elegir còmo quieres jugar. Elige una opcion:\n1). PvE (Jugador vs Entorno)\n2). JcJ (Jugador contra Jugador)\n--> "))
    if opc_user == 1:
        os.system("cls")
        while True:
            print("Antes de comenzar, es necesario registrarse.")
            rgstr_user = input("Ingrese su nombre de usuario: ")
            users = {
                'name' : rgstr_user
            }
            input("Usuario registrado con éxito. Presiona Enter para continuar --> ")
            os.system('cls')
            user = input("Elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n ").capitalize()
            opc = ["Piedra","Papel","Tijeras"]
            # if user != "Piedra" or user != "Papel" or user != "Tijeras": return print("Elección no válida, intentalo de nuevo.")
            env = random.choice(opc)
            if user == "Piedra" and env == "Tijeras":
                print(f"¡{user} aplasta {env}! ¡Lo hiciste genial, esta ronda es tuya!")
            elif user == "Papel" and env == "Piedra":
                print(f"¡{user} envuelve {env}! ¡Muy bien, esta vez ganaste tú!")
            elif user == "Tijera" and env == "Papel":
                print(f"¡{user} corta {env}! ¡Buena jugada, te llevas la victoria!")
            elif env == "Piedra" and user == "Tijeras":
                print(f"¡{env} aplasta {user}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!")
            elif env == "Papel" and user == "Piedra":
                print(f"¡{env} envuelve {user}! Has perdido esta vez.")
            elif env == "Tijera" and user == "Papel":
                print(f"¡{env} corta {user}! No te preocupes, ¡a la siguiente lo conseguirás!")
    if opc_user == 2:
        pass

    