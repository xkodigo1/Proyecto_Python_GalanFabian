import os, platform # Platform, modulo para reconocer el SO del usuario
import modules as pack
def menuP():
        print(pack.ttl_menuP)
        input("¡Bienvenido a The Chachipun! ¿Preparado para poner a prueba tu suerte mediante una elecciòn?\nPresiona Enter para continuar --> ")
        while True:
            os.system("cls" if platform.system() == "Windows" else "clear") # Condicion que verifica el SO del usuario para limpiar la consola de la manera en que el SO lo requiera
            opc_user = int(input("Es hora de elegir còmo quieres jugar. Elige una opcion:\n1). PvE (Jugador vs Entorno)\n2). JcJ (Jugador contra Jugador)\n--> "))
            os.system("cls" if platform.system() == "Windows" else "clear")
            if opc_user == 1:
                pack.JvE()
            elif opc_user == 2:
                pack.JcJ()
    