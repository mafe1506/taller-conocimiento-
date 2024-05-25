n = int(input("Ingrese la cantidad de números en la lista: "))

numeros = []

for i in range(n):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

print("Valores al cuadrado:")
for num in numeros:
    print(num, "elevado al cuadrado es:", num**2)