numeros_str = input("Ingresa los números que deseas sumar, separados por espacios: ")

numeros = numeros_str.split()

lista_numeros = []

for num in numeros:
    lista_numeros.append(float(num))

suma_total = sum(lista_numeros)

print("La suma de los números en la lista es:", suma_total)
