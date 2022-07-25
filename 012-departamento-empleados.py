empresa = []
dpto1 = []
dpto2 = []
empleadosdep1 = []
empleadosdep2 = []
e1 = ["Director","Luis"]
e2 = ["Técnico","Pablo"]
e3 = ["Gerente","Paula"]
e4 = ["Publicista","Andrea"]
e5 = ["Escritor","Pedro"]
#Insertar departamentos a la empresa
empresa.append(dpto1)
empresa.append(dpto2)
#Poner el nombre al departamento 1
dpto1.append("Informática")
#Asignar empleados al departamento 1
empleadosdep1.append(e1)
empleadosdep1.append(e2)
dpto1.append(empleadosdep1)
#Poner nombre al departamento 2
dpto2.append("Ventas")
#Asignar empleados al departamento 2
empleadosdep2.append(e3)
empleadosdep2.append(e4)
empleadosdep2.append(e5)
dpto2.append(empleadosdep2)
#Cambio gerente departamento de ventas
e3[1] = "María"
#Mostrar la empresa
for departamento in empresa:
    print("======",departamento[0],"======")
    for empleado in departamento[1]:
        print("   -",empleado[0]+":",empleado[1])
#Buscar la profesion de un empleado
nombre_a_buscar = input("Introduce el nombre del empleado a buscar: ")
for departamento in empresa:
    for empleado in departamento[1]:
        if empleado[1] == nombre_a_buscar:
            print(empleado[1],"trabaja como",empleado[0],"en el departamento de",departamento[0])