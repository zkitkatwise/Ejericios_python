import random
planetas = ["Mercurio","Venus","Marte","Jupiter","Saturno","Urano","Neptuno","Pluton"]
planeta_secreto=random.choice(planetas)
numIntentos=1
print(planetas)
planeta_candidato=input("Adivina en qué planeta estoy pensando: ").capitalize()
while planeta_candidato!=planeta_secreto:
    print("--No has acertado--")
    planetas.remove(planeta_candidato)
    numIntentos+=1
    print(planetas)
    planeta_candidato=input("Adivina en qué planeta estoy pensando: ").capitalize()
else:
    print("¡Has acertado! Lo has adivinado en",numIntentos,"intentos.")