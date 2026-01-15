a = 3
b = 4

resultado = 0
operacion = ""
i = 0

while i < b:
    resultado += a
    operacion += str(a)
    if i < b - 1:
        operacion += "+"
    i += 1

print(f"{operacion}={resultado}")