import datetime as dt

nombre="Zkitkat Superwise"
año_nacimiento=2000
email="holaquetal@hola.com"
num_telefono="17293102"
año_actual = dt.date.today().year
edad = año_actual-año_nacimiento

nombre_es_correcto = len(nombre)>=10
edad_es_valida = edad>=18
email_es_correcto = "@" in email
num_tlf_es_correcto = num_telefono.isnumeric()

#Solución 1 (sin decir qué es incorrecto)
"""
if nombre_es_correcto and edad_es_valida and email_es_correcto and num_tlf_es_correcto:
    print("Formulario válido")
else:
    print("El formulario no es valido")
"""

#Solución 2 (else se ejecuta siempre que el tlf. sea correcto, incluso si hay algo mal)
"""
if not nombre_es_correcto:
    print("El nombre tiene que ser mayor de 10 caracteres")
if not edad_es_valida:
    print("Tienes que ser mayor de edad")
if not email_es_correcto:
    print("Introduce una dirección de correo electronico válida")
if not num_tlf_es_correcto:
    print("El número de teléfono es incorrecto")
else:
    print("Formulario válido")
"""

#Solución 3
hayError=False #Flag
if not nombre_es_correcto:
    print("El nombre tiene que ser mayor de 10 caracteres")
    hayError=True
if not edad_es_valida:
    print("Tienes que ser mayor de edad")
    hayError=True
if not email_es_correcto:
    print("Tiene que introducir una dirección de correo electronico válida")
    hayError=True
if not num_tlf_es_correcto:
    print("El número de teléfono es incorrecto")
    hayError=True
if not hayError:
    print("Formulario válido")