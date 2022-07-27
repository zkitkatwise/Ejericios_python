import winsound

TIEMPO_SONIDO=1000
peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu altura (metros): "))
imc=peso/altura**2
print("Tu IMC es:",imc)

if imc>=40:
    estado="Obesidad muy severa"
elif imc>=35:
    estado="Obesidad severa"
elif imc>=30:
    estado="Obesidad moderada"
elif imc>=25:
    estado="Sobrepeso"
elif imc>=18.5:
    estado="Peso saludable"
elif imc>=16:
    estado="Delgadez"
elif imc>=15:
    estado="Delgadez severa"
else:
    estado="Delgadez muy severa"

print("Tu estado es:",estado)
winsound.Beep(int(imc)*10,TIEMPO_SONIDO)