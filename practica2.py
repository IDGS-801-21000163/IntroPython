import os


def suma(a, b):
    return a + b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    return a/b

def salir():
    os.system('clear')

def menu():
    os.system('clear')

    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))

    print("Menú\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir")
    opcion = int(input('Ingrese la opción:'))

    if (opcion == 1):
        resultado = suma(num1, num2)
    if (opcion == 2):
        resultado = resta(num1, num2)
    if (opcion == 3):
        resultado = multiplicacion(num1, num2)
    if (opcion == 4):
        resultado = division(num1, num2)
    if (opcion == 5):
        salir()
        return

    print("El resultado es ", resultado)

if __name__ == '__main__':
    menu()