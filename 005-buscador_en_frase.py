frase="En un lugar de La Mancha, La Mancha es una región"
fraseMayusc=frase.upper()
TextoABuscar=input("¿Qué quieres buscar?: ")
TextoABuscarMayusc=TextoABuscar.upper()
NumCoincidencias=fraseMayusc.count(TextoABuscarMayusc)
print("El texto \""+TextoABuscar+"\"","aparece",NumCoincidencias,end="")
if NumCoincidencias==1:
    print(" vez.")
else:
    print(" veces.")