import generador_cosas_aleatorias as cosa_aleatoria

NUM_CARACTERES_CONTRASEÑA = 8
NOMBRE_ARCHIVO = "tabla-contraseñas-nombres-random.csv"
NUMERO_ELEMENTOS = 100

fichero_csv = open(NOMBRE_ARCHIVO,"w")
fichero_csv.write("NOMBRE;CONTRASEÑA\n")

for n in range(NUMERO_ELEMENTOS):
    fichero_csv.write(str(cosa_aleatoria.generar_nombre(1)+";"+cosa_aleatoria.generar_contraseña(NUM_CARACTERES_CONTRASEÑA)+"\n"))

fichero_csv.close
print("DONE")