import json
import os 

data_game = {
    "JcJ" : {
        "nickname_u_u" : {
            "vic_user_u" : 0,
            "def_user_u" : 0
        },
        "nickname_u_d" : {
            "vic_user_d" : 0,
            "def_user_d" : 0
        },
    "PvE" : {
        "nickname_u" : {
            "vic_user" : 0,
            "def_user" : 0
        },
        "environment" : {
            "vic_env" : 0,
            "def_env" : 0
        }
    }
    }

}
with open ("data/data_game.json" "w+") as file:
    json.load(file, indent=4)
    





# with open("data/ejemplo.json", "r") as file:
#    archivo = json.load(file) 

# archivo["Jugadores"].append("MAURICIO")
# archivo["Partidas_totales"] = {}

# print(json.dumps(archivo, indent=4))

# with open("data/ejemplo.json", "w") as file:
#    json.dump(archivo, file, indent=4)
#    file.close()
#print('holaa', json.dumps(archivo, indent=4))

# dump -> Escribir la data en el file
# dumps -> serializar la data, devuelve una cadena que contiene la representación JSON del objeto.