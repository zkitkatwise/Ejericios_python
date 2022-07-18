num1 = float(input("Introduzca la primera cantidad: "))
num2 = float(input("Introduzca la segunda cantidad: "))
impuesto = float(input("Introduzca el porcentaje de impuestos: "))/100
importe = num1+num2+(num1+num2)*impuesto
print("El importe es",importe,"€.")