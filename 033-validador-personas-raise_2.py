class ValidationError(Exception):
     def __init__(self,mensaje): 
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def validador_personas(nombre:str,edad:int,color:str):
    colores_denegados = ["Naranja"]
    if len(nombre)<3:
        raise ValidationError("El nombre es muy corto")
    if edad<18:
        raise ValidationError("Eres menor de edad")
    if color.lower().capitalize() in colores_denegados:
        raise ValidationError("Tienes un gusto horrible con los colores")


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
color_fav = input("Introduce tu color favorito: ")

try:
    validador_personas(nombre,edad,color_fav)
except ValidationError as validation_err:
    print(validation_err.mensaje)
else:
    print("Has pasado!")