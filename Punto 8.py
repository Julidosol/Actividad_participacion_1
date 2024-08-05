print("Hola, Vamos a invertir los numeros de la lista que indiques")
cantidad_numeros = input("Ingrese cuantos numeros deseas tener en la lista")
cantidad_numeros = int(cantidad_numeros)

numeros=[]
for i in range(cantidad_numeros):
    numero=int(input("ingrese un numero "))
    numeros.append(numero)
numeros.reverse()
print(numeros)