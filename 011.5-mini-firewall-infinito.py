NUMERO_INTENTOS = 3
EXIT = "0"
ip="-1"
peticiones = []
lista_negra = []
while ip!=EXIT:
    ip=input("Introduce una dirección IP: ")
    if (ip in lista_negra):
        print("¡Ataque detectado!","IP de origen: "+ip)
    elif (ip!=EXIT):
        peticiones.append(ip)
        if (peticiones.count(ip)==NUMERO_INTENTOS):
            lista_negra.append(ip)