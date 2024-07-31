print("Hola, Vamos a determinar si un numero es par o impar")
numero = input("Ingrese un numero ")
numero = int(numero)
divisor = int(2)
if numero % divisor == 0:
    print("El numero es par") 
else:
    print("El numero es impar")