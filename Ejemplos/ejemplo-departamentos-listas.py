#Empleados Departamento 1
empleado1dep1=["Pepe","Administrador"]
empleado2dep1=["María","Jefa"]
empleadosdep1=[empleado1dep1,empleado2dep1]
#Empleados Departamento2
empleado1dep2=["Luis","Consultor"]
empleado2dep2=["Alba","Secretaria"]
empleado3dep2=["Pedro","Abogado"]
empleadosdep2=[empleado1dep2,empleado2dep2,empleado3dep2]
#Departamentos
dep1=["Departamento 1",empleadosdep1]
dep2=["Departamento 2",empleadosdep2]
#Empresa
empresa=[dep1+dep2]
print(empresa)