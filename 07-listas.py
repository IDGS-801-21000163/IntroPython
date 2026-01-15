mi_lista = [1,2,3,4,5,6,7,8,9,10]
print(type(mi_lista))
print(mi_lista)
print(mi_lista[1])
print(mi_lista[2])
print(mi_lista[-1])
print(mi_lista[4:])

lista_uno=["Dario", 33, 8.5, True, "German", 20.8]

lista_uno.append("Vargas")
print(lista_uno)

lista_uno.insert(2, "Nadia")
print(lista_uno)

lista_uno.extend(["uno", 1.1, False])
print(lista_uno)

lista_uno.remove(33)
print(lista_uno)

lista_uno.pop()
print(lista_uno)

lista_dos = ["tres", "cuatro"]
lista_tres = lista_uno + lista_dos
print(lista_tres)

lista_cuatro = [2, 1, 5, 4, 3]
print(lista_cuatro)
print(lista_cuatro.sort())

del lista_cuatro[0]
print(lista_cuatro)