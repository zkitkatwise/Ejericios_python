dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
dia_elegido = input("Introduce un dia de la semana: ").lower()
for dia in dias:
    if dia_elegido==dia:
        print("Es el",dia_elegido.capitalize())
        break
    else:
        print(dia.capitalize(),"no es")