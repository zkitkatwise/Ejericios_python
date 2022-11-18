def calcular(*numeros):
    print("----------------")
    for valor in numeros:
        print(str(valor))

calcular()
calcular(1)
calcular(1,"algo")
calcular(1,"algo",False)
calcular(1,"algo",False,["Lunes","Martes"])