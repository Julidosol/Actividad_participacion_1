print("Hola, Vamos a hacer el cambio de grados Fahrenheit a grados Celsius")
def grados_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return celsius 

fahrenheit = input(" Ingresa los grados en Fahrenheit ")
fahrenheit = int(fahrenheit)
celsius = grados_celsius(fahrenheit)
print(celsius)
