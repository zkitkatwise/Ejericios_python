#PARTE UNO
import urllib.request
print("Leyendo URL...")
webUrl  = urllib.request.urlopen('https://www.gutenberg.org/files/2000/2000-0.txt')
texto = webUrl.read()
#PARTE DOS
texto = str(texto)
texto_minusculas = texto.lower()
#PARTE TRES
texto_lista = texto_minusculas.split()
#PARTE CUATRO
palabra = input("Introduce la palabra a buscar: ")
palabra = palabra.lower()
numcoincidencias = texto_minusculas.count(palabra)
print("La palabra \""+palabra+"\" aparece",numcoincidencias,"veces.")
#PARTE CUATRO (LISTA)
numcoincidenciaslista = texto_lista.count(palabra)
print("La palabra \""+palabra+"\" aparece",numcoincidenciaslista,"veces en la lista.")
#PARTE CINCO
if palabra in texto_lista:
    print("\""+palabra.capitalize()+"\"","está en el Quijote")
else:
    print("\""+palabra.capitalize()+"\"","no está en el Quijote")
