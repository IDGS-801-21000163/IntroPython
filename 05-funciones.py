import os

def saludar(nombre):
    return f"Hola {nombre}"

def sumar(a, b):
    return a+b


os.system('clear')
saludar('Ana')
input("Presiona Enter para salir...")


def main():
    os.system('clear')
    print(saludar('Juan'))
    resultado_suma = sumar(5, 7)
    print("La suma de 5 y 7 es:", resultado_suma)
    input("Presiona Enter para salir...")

if __name__ == '__main__':
    main()