print("Hola, vamos a calcular el area de un circulo dado su radio ")
def area_circulo_radio(radio):
    radio = int(radio)
    radiocuadrado = (radio * radio)
    pi = 3.14159
    area = int(radiocuadrado * pi)
    return area


radio = input("Ingresa el radio del circulo ")
area = area_circulo_radio(radio)
print("El area del circulo con radio ", radio, "es de: ", area)