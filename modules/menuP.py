import os
import modules as pack
def menuP():
        print(pack.ttl_menuP)
        input("¡Bienvenido a Rock, Paper N' Scissors! ¿Preparado para poner a prueba tu suerte mediante una elecciòn?\nPresiona Enter para continuar --> ")
        os.system("cls")
        while True:
            opc_user = int(input("Es hora de elegir còmo quieres jugar. Elige una opcion:\n1). PvE (Jugador vs Entorno)\n2). JcJ (Jugador contra Jugador)\n--> "))
            os.system("cls")
            if opc_user == 1:
                pack.JvE()
            elif opc_user == 2:
                pack.JcJ()
    