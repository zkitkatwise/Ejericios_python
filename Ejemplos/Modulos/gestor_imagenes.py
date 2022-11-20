#import {nombre_carpeta}.{nombre_libreria}
import librerias_personales.descargador_imagenes as descargador_img

url = input("Introduce la URL de la imagen: ")
nombre_fichero = input("Introduce el nombre del fichero a crear y su extensión: ")

#librerias_personales.descargador_imagenes.get_image_from_url(url,nombre_fichero)
descargador_img.get_image_from_url(url, nombre_fichero)