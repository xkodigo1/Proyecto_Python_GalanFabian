# pass
# cntdr_jcj = {
#     'rnds_gu_u' : 0,
#     'rnds_gu_d' : 0
# }
# if pass == 2:
# print("Antes de comenzar, es necesario registrarse.")
#         rgstr_userU = input("Ingrese el nombre del jugador 1: ")
#         rgstr_userD = input("Ingrese el nombre del jugador 2: ")
#         users = {
#             'nameU' : rgstr_userU,
#             'nameD' : rgstr_userD
#         }
#         input("Usuarios registrados con éxito. Presiona Enter para continuar --> ")
#         os.system('clear')
#         vicConsUserUno = 0
#         vicConsUserDos = 0
#         while True:
#             if cntdr_jcj['rnds_gu_u'] < 3 and cntdr_jcj['rnds_gu_d'] < 3:
#                 user_u = input(f"---------------------------------\n{users['nameU']} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
#                 user_d = input(f"---------------------------------\n{users['nameD']} elige una opción:\n--> Piedra\n--> Papel\n--> Tijeras\n---------------------------------\n").upper()
#                 if user_u == "PIEDRA" and user_d == "TIJERAS":
#                     if vicConsUserDos >= 2: 
#                         print(f"¡{users['nameD']} tenía un escudo activo! {users['nameU']}Aunque ganaste esta ronda, no obtienes puntos.")
#                         vicConsUserDos = 0
#                         vicConsUserUno += 1
#                         continue
#                     vicConsUserUno += 1
#                     cntdr_jcj['rnds_gu_u'] += 1
#                     print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_u == "PAPEL" and user_d == "PIEDRA":
#                     if vicConsUserDos >= 2: 
#                         print(f"¡{users['nameD']} tenía un escudo activo! {users['nameU']}Aunque ganaste esta ronda, no obtienes puntos.")
#                         vicConsUserDos = 0
#                         vicConsUserUno += 1
#                         continue
#                     vicConsUserUno += 1
#                     cntdr_jcj['rnds_gu_u'] += 1
#                     print(f"¡{user_u} aplasta {user_d}! ¡Lo hiciste genial, esta ronda es tuya!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_u == "TIJERAS" and user_d == "PAPEL":
#                     if vicConsUserDos >= 2: 
#                         print(f"¡Entorno tenía un escudo activo! Aunque ganaste esta ronda, no obtienes puntos.")
#                         vicConsUserDos = 0
#                         vicConsUserUno += 1
#                         continue
#                     vicConsUserUno += 1
#                     cntdr_jcj['rnds_gu_u'] += 1
#                     print(f"¡{user_u} corta {user_d}! ¡Buena jugada, te llevas la victoria!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_d == "PIEDRA" and user_u == "TIJERAS":
#                     if vicConsUserUno >= 2: 
#                         print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
#                         vicConsUserUno = 0
#                         vicConsUserDos += 1
#                         continue
#                     vicConsUserDos += 1
#                     cntdr_jcj['rnds_gu_d'] += 1
#                     print(f"¡{user_d} aplasta {user_u}! Esta vez no fue la tuya, ¡pero la próxima seguro lo es!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_d == "PAPEL" and user_u == "PIEDRA":
#                     if vicConsUserUno >= 2: 
#                         print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
#                         vicConsUserUno = 0
#                         vicConsUserDos += 1
#                         continue
#                     vicConsUserDos += 1
#                     cntdr_jcj['rnds_gu_d'] += 1
#                     print(f"¡{user_d} envuelve {user_u}! Has perdido esta vez.\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_d == "TIJERAS" and user_u == "PAPEL":
#                     if vicConsUserUno >= 2: 
#                         print(f"{users['name']} tenía un escudo activo! Aunque Entorno ganó esta ronda, no obtendra puntos.")
#                         vicConsUserUno = 0
#                         vicConsUserDos += 1
#                         continue
#                     vicConsUserDos += 1
#                     cntdr_jcj['rnds_gu_d'] += 1
#                     print(f"¡{user_d} corta {user_u}! No te preocupes, ¡a la siguiente lo conseguirás!\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_u == user_d:
#                     print(f"¡Empate! Ambos eligieron lo mismo. ¡Parece que están en sintonía! ¿Vamos de nuevo?\nMARCADOR: {cntdr_jcj['rnds_gu_u']} - {cntdr_jcj['rnds_gu_d']}")
#                 elif user_u not in opc or user_d not in opc:
#                     input("Elección no válida. Presiona Enter para regresar --> ")
#             else: 
#                 print(f"{users['nameU']} es el ganador" if cntdr_jcj['rnds_gu_u'] > cntdr_jcj['rnds_gu_d'] else f"{users['nameD']} es el ganador")
#                 break