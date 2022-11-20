import requests
URL_IMAGEN= "https://images.alphacoders.com/115/1156309.jpg" #He cogido una imagen cualquiera de internet

with open("imagen_salida.jpg","wb") as archivo:
    rq = requests.get(URL_IMAGEN,allow_redirects=True)
    archivo.write(rq.content)