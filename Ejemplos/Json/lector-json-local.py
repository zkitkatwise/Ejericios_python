import json

pelicula = input("Introduce el título de la película a buscar: ")
try:
    with open(pelicula+".json","r") as archivo:
        texto_basico = archivo.read()
        #Str con el json en texto plano
        diccionario = json.loads(texto_basico)
        #Diccionario con la informacion del json
        print("El director de {} es {}. La película salió en {}.".format(diccionario["Title"],diccionario["Director"],diccionario["Year"]))
        print("----------------------------------------------------------------------------------------")
        for lista in diccionario["Ratings"]:
            print(f"La pelicula ha obtenido una valoración de {lista['Value']} en {lista['Source']}.")

except FileNotFoundError:
    print("El archivo de la película no se encontró")
except:
    print("Ha ocurrido un error inesperado")