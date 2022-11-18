import json
import urllib.request

def obtener_dicc_archivo_json(archivo):
    with open(archivo,"r") as archivo:
        diccionario = json.load(archivo)
        return diccionario
def obtener_dicc_json_url(url):
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    diccionario = json.loads(data) #Método "loads" convierte los bytes directamente
    return diccionario

#Obtenemos diccionario de un archivo .json almacenado en el ordenador:
#datos = obtener_dicc_archivo_json("dracula.json")
#Obtenemos dicciomario de un .json almacenado en una web(URL):
datos = obtener_dicc_json_url("https://it-python-admin.github.io/peliculas/indiana-last-crusade.json")

print("El director de {} es {}. La película salió en {}.".format(datos["Title"],datos["Director"],datos["Year"]))
print("----------------------------------------------------------------------------------------")
for lista in datos["Ratings"]:
    print(f"La pelicula ha obtenido una valoración de {lista['Value']} en {lista['Source']}.")