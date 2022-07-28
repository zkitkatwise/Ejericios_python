import datetime as dt

año_nacimiento = int(input("Introduce tu año de nacimiento: "))
año_actual = dt.date.today().year
edad = año_actual-año_nacimiento
if edad>=65:
    estado="Jubilado"
elif edad>40:
    estado="Adulto"
elif edad>=18:
    estado="Joven"
else:
    estado="Menor de edad"

print("Franja:",estado)