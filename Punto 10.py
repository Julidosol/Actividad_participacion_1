print("Vamos a calcular el factorial de un numero")


def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
resultado = factorial(numero)
print(f"El factorial de", numero, "es:", resultado")