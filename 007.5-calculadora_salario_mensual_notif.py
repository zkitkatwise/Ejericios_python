from win10toast import ToastNotifier
salarioAnual=input("¿Cuál es tu salario anual?: ")
if salarioAnual.isdigit():
    salarioAnual=int(salarioAnual)
    numMeses=int(input("¿En cuántas pagas quieres calcularlo? (12 o 14): "))
    salarioMensual=(salarioAnual/numMeses)
    print("Tu salario mensual es",salarioMensual,"€ en",numMeses,"pagas.")
    toaster= ToastNotifier()
    toaster.show_toast("Zkit Project","Tu salario mensual es "+str(salarioMensual))
elif salarioAnual[0]=="-":
    print("El valor introducido no es positivo.")
else:
    print("El valor que has introducido no es un número.")