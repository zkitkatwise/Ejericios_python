animales = ["Dog","Cat","Bird","Cow","Snake"]
animal_elegido = input("Introduce el nombre de un animal en inglés: ").capitalize()
while animal_elegido not in animales:
    print("Ese animal no está en la lista")
    animal_elegido = input("Introduce el nombre de un animal en inglés: ").capitalize()
else:
    print("¡Acertaste!")
print("Juego terminado")