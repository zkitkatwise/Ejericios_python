nombre=input("Escribe tu nombre: ")
edad=input("Introduce tu edad: ")
edad=int(edad)
if edad>=18:
    print("¡Enhorabuena",nombre+"! ¡Eres mayor de edad!")
else:
    print("Vaya,",nombre,",todavía no eres mayor de edad.")