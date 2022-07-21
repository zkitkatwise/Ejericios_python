empresa=[]
departamento1=["Informatica"]
departamento2=["Recursos Humanos"]
empleado1=["Pablo","Director"]
empleado2=["Sofia","Subdirectora"]
empleado3=["Lucas","Técnico"]
empleado4=["Lucía","Directora"]
empleado5=["Luis","Técnico"]
empleados_dpto1=[empleado1,empleado2]
empleados_dpto2=[empleado3,empleado4,empleado5]
departamento1.append(empleados_dpto1)
departamento2.append(empleados_dpto2)
empresa.append(departamento1)
empresa.append(departamento2)
for departamento in empresa:
    print("Departamento:",departamento[0])
    for empleado in departamento[1]:
        print(" *Empleado*: ",empleado[0])
        print("   -Categoria-: ",empleado[1])