import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    resumen=resumen.hexdigest()
    return resumen

ficheroEntrada = input("Introduce el nombre del fichero de contraseñas: ")
ficheroSalida = input("Introduce el nombre del fichero a crear con los hash: ")

fRead = open(ficheroEntrada,"r")
fOut = open(ficheroSalida,"w")

pwd=fRead.readline()
while pwd:
    pwdHash = obtener_hash(pwd.replace("\n",""))
    fOut.write(pwdHash)
    fOut.write("\n")
    pwd=fRead.readline()
fRead.close()
fOut.close()