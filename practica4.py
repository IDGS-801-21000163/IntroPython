lista = []

for i in range(0, 20):
    num = int(input("Ingrese un numero (" + str(i) + "): "))
    lista.append(num)

print(lista)
lista.sort()
print(lista)

recorridos = []
for i in lista:
    if i in recorridos:
        continue

    recorridos.append(i)
    if lista.count(i) > 1:
        print("El numero " + str(i) + " se repitió " + str(lista.count(i)) + " veces")

pares = []
impares = []
for recorrido in recorridos:
    if recorrido % 2 == 0:
        pares.append(recorrido)
    else:
        impares.append(recorrido)

print(pares)
print(impares)