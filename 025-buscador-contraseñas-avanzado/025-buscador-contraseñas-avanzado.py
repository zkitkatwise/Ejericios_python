import hashlib

def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()

fichero = input("Introduce el nombre del archivo con los hash: ")
contraseña = input("Introduce una contraseña a buscar: ")

hash_contraseña = obtener_hash(contraseña)
fichero = open(fichero)
hash_leido = fichero.readline().replace("\n","")
while hash_leido:
    if hash_leido==hash_contraseña:
        print("La contraseña está en el archivo, *NO* la uses")
        break
    hash_leido = fichero.readline().replace("\n","")
else:
    print("La contraseña no está en el archivo, puedes usarla")
fichero.close()