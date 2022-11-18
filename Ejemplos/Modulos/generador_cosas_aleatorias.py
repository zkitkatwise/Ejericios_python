import random

nombres = ("Juan","Javier","Luis","Antonio","Oscar","Martin","Pablo","Alvaro","Fernando")
apellidos = ("Garcia","Revuelta","Cantera","de la Mata","Martin","Guttierez","Arboleda", "Perez","Mendez","Ramos")

def generar_lista_personas(numero):
    for i in range(numero):
        nueva_persona = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        print(nueva_persona)

def generar_contraseña(num_caracteres):
    contraseña = ""
    vocales_min = "aeiou"
    vocales_mayus = vocales_min.upper()
    consonantes_min = "zyxwvtrsqpñnmlkjhgfdcb"
    consonantes_mayus = consonantes_min.upper()
    digitos = "0123456789"
    caracteres_especiales = "@#-_%"
    opciones = [vocales_mayus,vocales_min,consonantes_min,consonantes_mayus,digitos,caracteres_especiales]
    for i in range(num_caracteres):
        caracter_aleatorio = random.choice(random.choice(opciones))
        contraseña = contraseña + caracter_aleatorio
    return contraseña

#print(generar_contraseña(20))
#generar_lista_personas(8)