def sumar(s1,s2):
    return s1+s2
def restar(r1,r2):
    return r1-r2
def multiplicar(m1,m2):
    return m1*m2
def dividir(d1,d2):
    return d1/d2

def mostar_menu():
    print("\n1.Sumar","2.Restar","3.Multiplicar","4.Dividir","0.Salir","",sep="\n")

def gestion_operaciones(operacion,operando1,operando2):
    if operacion==1:
        resultado = sumar(operando1,operando2)
    elif operacion==2:
        resultado = restar(operando1,operando2)
    elif operacion==3:
        resultado = multiplicar(operando1,operando2)
    elif operacion==4:
        resultado = dividir(operando1,operando2)
        
    return resultado

operacion = -1
while operacion!=0:
    mostar_menu()
    try:
        operacion=int(input("Introduce el número de la operación: "))
        if operacion!=0:
            operando1=int(input("Introduce el primer operando: "))
            operando2=int(input("Introduce el segundo operando: "))
            resultado = gestion_operaciones(operacion,operando1,operando2)
            print("\n---- El resultado de la operación es:",resultado,"----")
    except:
        print("\nSe ha producido un error","")