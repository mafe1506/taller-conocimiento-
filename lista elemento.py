elementos = input("Ingrese una lista de elementos separados por espacios: ").split()

elemento_a_buscar = input("Ingrese el elemento que desea buscar: ")

posiciones = []

for i, elemento in enumerate(elementos):
    if elemento == elemento_a_buscar:
        posiciones.append(i)

if len(posiciones) == 0:
    print("El elemento no se encuentra en la lista.")
else:
    print("El elemento", elemento_a_buscar, "se encuentra en la(s) posición(es):", posiciones)