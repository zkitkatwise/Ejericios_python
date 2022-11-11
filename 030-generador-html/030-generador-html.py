NOMBRE_ARCHIVO = "salida.html"

datos =(("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000),
        ("Enero",10000),("Febrero",3000),("Marzo",5000))

archivo = open(NOMBRE_ARCHIVO,"w")
archivo.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <title>Tabla de ventas</title>
</head>
<body>
    <h1>Ventas anuales</h1>
    <table>
        <tr>
            <td>Mes</td>
            <td>Ventas</td>
        </tr>""")
for item in datos:
    archivo.write(f"""<tr>
            <td>{item[0]}</td>
            <td>{item[1]}</td>
        </tr>""")
archivo.write("""    </table>
</body>
</html>""")
archivo.close()
print("DONE")