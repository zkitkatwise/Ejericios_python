from re import A


numeros = [3,8,10,23,0]
try:
    num1 = int(input("Introduce un numero entre 0 y 4: "))
    num2 = int(input("Introduce otro numero entre 0 y 4: "))
    resultado = numeros[num1]/numeros[num2]

except ValueError:
    print("El valor introducido no es un número.")
except IndexError:
    print("El numero introducido está fuera de rango.")
except ZeroDivisionError:
    print("No se puede dividir entre 0.")
except:
    print("Ha ocurrido un error desconocido")
else:
    print(resultado)