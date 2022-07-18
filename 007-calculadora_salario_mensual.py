salarioAnual=input("¿Cuál es tu salario anual?: ")
if salarioAnual.isdigit():
    salarioAnual=int(salarioAnual)
    numMeses=int(input("¿En cuántas pagas quieres calcularlo? (12 o 14): "))
    salarioMensual=round(salarioAnual/numMeses,1)
    print("Tu salario mensual es",salarioMensual,"€ en",numMeses,"pagas.")
elif salarioAnual[0]=="-":
    print("El valor introducido no es positivo.")
else:
    print("El valor que has introducido no es un número.")