print("Vamos a indicar el numero mayor y menor de la lista que indiques")
cantidad_numeros = input("Indica cuantos numeros quieres en la lista")
cantidad_numeros = int(cantidad_numeros)
numeros=[]
for i in range(cantidad_numeros):
    numero=int(input("ingrese un numero"))
    numeros.append(numero)
print("el menor es:",min(numeros))
print("el menor es:",max(numeros))