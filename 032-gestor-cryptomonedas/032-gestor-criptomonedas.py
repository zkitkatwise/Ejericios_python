NOMBRE_ARCHIVO = "cotizacion.dat"
NOMBRE_ARCHIVO_MONEDAS_POSITIVAS = "ventas-positivas.dat"
NOMBRE_ARCHIVO_MONEDAS_NEGATIVAS = "ventas-negativas.dat"

def obtener_monedas(nombre_archivo):
    monedas = []
    with open(nombre_archivo,"r") as archivo:
        nombre_moneda = archivo.readline().replace("\n","")
        while nombre_moneda!="":
            simbolo_moneda = archivo.readline().replace("\n","")
            cotizacion_moneda = float(archivo.readline().replace("\n",""))
            monedas.append((nombre_moneda,simbolo_moneda,cotizacion_moneda))
            nombre_moneda = archivo.readline().replace("\n","")
    return monedas
def obtener_monedas_negativas(datos):
    monedas_negativas = []
    for moneda in datos:
        variacion = moneda[2]
        if variacion<0:
            monedas_negativas.append(moneda)
    return monedas_negativas
def obtener_monedas_positivas(datos):
    monedas_positivas = []
    for moneda in datos:
        variacion = moneda[2]
        if variacion>0:
            monedas_positivas.append(moneda)
    return monedas_positivas
def nueva_orden_venta(moneda_negativa):
    for valor in moneda_negativa:
        print(f"Orden de venta de la moneda {valor[1]} ({valor[0]}), con una variacion de {valor[2]}")
def obtener_moneda(datos,nombre_moneda):
    for moneda in datos:
        if nombre_moneda==moneda[0]:
            return moneda[2]
def escribir_moneda_archivo(nombre_archivo,datos):
    with open(nombre_archivo,"w") as archivo:
        for valor in datos:
            archivo.write(f"Orden de venta de la moneda {valor[1]} ({valor[0]}), con una variacion de {valor[2]}\n")

monedas = obtener_monedas(NOMBRE_ARCHIVO)
monedas_negativas = obtener_monedas_negativas(monedas)
escribir_moneda_archivo(NOMBRE_ARCHIVO_MONEDAS_NEGATIVAS,monedas_negativas)
monedas_positivas = obtener_monedas_positivas(monedas)
escribir_moneda_archivo(NOMBRE_ARCHIVO_MONEDAS_POSITIVAS,monedas_positivas)
nueva_orden_venta(monedas_negativas)

moneda_consultada = input("Introduce el nombre de la moneda a buscar: ")
cotizacion = obtener_moneda(monedas,moneda_consultada)
print(("La cotizacion de *{0}* es *{1}*").format(moneda_consultada,cotizacion))