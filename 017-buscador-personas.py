personas = [
    ["Fernando",1971,"Madrid"],
    ["Francisco",1988,"Badajoz"],
    ["Javier",1990,"Tarragona"],
    ["Jose",1973,"Guadalajara"],
    ["Federica",1999,"Lugo"]
    ]

inicial=input("Introduce la inicial de tu nombre: ")
año_nacimiento=int(input("Introduce tu año de nacimiento: "))

for persona in personas:
    if persona[0].startswith(inicial.upper()):
        if año_nacimiento>persona[1]:
            print(persona[0])
        