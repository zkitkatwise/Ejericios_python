import urllib.request
print("Leyendo URL...")
webUrl  = urllib.request.urlopen('https://www.gutenberg.org/files/2000/2000-0.txt')
texto = webUrl.read()
texto = str(texto)
texto_minusculas = texto.lower()
texto_lista = texto.split()
palabra = input("Introduce la palabra a buscar: ")
palabra = palabra.lower()
numcoincidencias = texto_minusculas.count(palabra)
print("La palabra \""+palabra+"\" aparece",numcoincidencias,"veces.")
numcoincidenciaslista = texto_lista.count(palabra)
print("La palabra \""+palabra+"\" aparece",numcoincidenciaslista,"veces en la lista.")
if palabra in texto_lista:
    print("\""+palabra.capitalize()+"\"","está en el Quijote")
else:
    print("\""+palabra.capitalize()+"\"","no está en el Quijote")
