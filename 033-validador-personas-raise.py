class NombreCortoError(Exception):
    pass
class EdadInsuficienteError(Exception):
    pass
class MalGustoError(Exception):
    pass


def validador_personas(nombre:str,edad:int,color:str):
    colores_denegados = ["Naranja"]
    if len(nombre)<3:
        raise NombreCortoError
    if edad<18:
        raise EdadInsuficienteError
    if color.lower().capitalize() in colores_denegados:
        raise MalGustoError


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
color_fav = input("Introduce tu color favorito: ")

try:
    validador_personas(nombre,edad,color_fav)
except NombreCortoError:
    print("El nombre introducido es muy corto")
except EdadInsuficienteError:
    print("Eres menor de edad")
except MalGustoError:
    print("Tienes un gusto pésimo con los colores")
else:
    print("Has pasado!")