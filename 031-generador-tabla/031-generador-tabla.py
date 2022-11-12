NOMBRE_ARCHIVO = "Tabla.txt"

archivo = open(NOMBRE_ARCHIVO,"w")

ventas = {"Lunes":(2083,38), "Martes":(10,183), "Miércoles":(-283,19), "Jueves":(2023,11), "Viernes":(10,18)}

linea_dias = ""
linea1 = ""
linea2 = ""
for dia,valores in ventas.items():
    linea_dias = linea_dias + dia.ljust(10)
    linea1 = linea1 + str(valores[0]).rjust(10)
    linea2 = linea2 + str(valores[1]).rjust(10)

archivo.write("Ventas".center(50)+"\n")
archivo.write(linea_dias + "\n")
archivo.write(linea1 + "\n")
archivo.write(linea2 + "\n")

archivo.close()