NOMBRE_ARCHIVO = "cotizacion.dat"

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
def nueva_orden_venta(moneda_negativa):
    for valor in moneda_negativa:
        print(f"Orden de venta de la moneda {valor[1]} ({valor[0]}), con una variacion de {valor[2]}")
monedas = obtener_monedas(NOMBRE_ARCHIVO)
monedas_negativas = obtener_monedas_negativas(monedas)
nueva_orden_venta(monedas_negativas)