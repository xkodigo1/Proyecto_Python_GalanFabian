import json
import os 

""" with open("data/ejemplo.json", "r") as file:
    archivo = json.load(file) 

archivo["Jugadores"].append("MAURICIO")
archivo["Partidas_totales"] = {}

print(json.dumps(archivo, indent=4))

with open("data/ejemplo.json", "w") as file:
    json.dump(archivo, file, indent=4)
    file.close() """
#print('holaa', json.dumps(archivo, indent=4))

# dump -> Escribir la data en el file
# dumps -> serializar la data, devuelve una cadena que contiene la representación JSON del objeto.