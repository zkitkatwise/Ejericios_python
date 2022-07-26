coche1 = ["Toyota","RAV4","Verde"]
coche2 = ["Volkswagen","Taigo","Naranja"]
coche3 = ["Seat","León","Blanco"]
coches = {"9435KGJ":coche1,"2437QRT":coche2,"8774JBC":coche3}
matricula = input("Introduce la matricula a buscar: ")

if coches.get(matricula)==None:
    print("La matricula buscada no existe")
else:
    print(coches.get(matricula))

"""
#Solucion corta
if matricula in coches:
    print(coches[matricula])
else:
    print("La matricula buscada no existe")
"""