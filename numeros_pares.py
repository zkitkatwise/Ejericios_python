numeros_pares = []
numero=1
ultimonumero=int(input("Introduce el último número de tu lista: "))
while numero <= ultimonumero:
    if numero % 2 == 0:
        numeros_pares.insert(len(numeros_pares),numero)
        numero+=1
    else:
        numero+=1
print(numeros_pares)