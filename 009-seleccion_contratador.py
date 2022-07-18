MAYORIAEDAD = 18
edad = int(input("Introduce tu edad: "))
nacionalidad = input("¿Cuál es tu nacionalidad?: ")
idioma1 = input("¿Qué primer idioma hablas?: ")
idioma2 = input("¿Qué segundo idioma hablas?: ")
mayor_edad = edad>=MAYORIAEDAD
nacionalidad_valida = (nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad!="Ruso"
idiomas_validos = idioma1=="Ingles" and idioma2=="Chino" or idioma1=="Chino" and idioma2=="Ingles"

if mayor_edad and nacionalidad_valida and idiomas_validos:
    print("Puedes ser contratado")
else:
    print("No cumples el perfil")