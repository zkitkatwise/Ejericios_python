NUMERO_INTENTOS = 3
peticiones=[]
lista_negra=[]
ip=-1
while ip not in lista_negra:
    ip=input("Introduce una dirección IP: ")
    peticiones.append(ip)
    if peticiones.count(ip)>=NUMERO_INTENTOS:
        lista_negra.append(ip)

if ip in lista_negra:
    print("¡Ataque detectado!","IP de origen: "+ip)