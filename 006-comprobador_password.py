PALABRA_PROHIBIDA1="ADMIN"
PALABRA_PROHIBIDA2="123"
PALABRA_PROHIBIDA3="PASSWORD"

idUsuario=input("Introduce tu usuario: ")
password=input("Introduce tu contraseña: ")

if PALABRA_PROHIBIDA1 in password:
    print("La contraseña no es válida")
elif PALABRA_PROHIBIDA2 in password:
    print("La contraseña no es válida")
elif PALABRA_PROHIBIDA3 in password:
    print("La contraseña no es válida")
else:
    print("La contraseña es válida")