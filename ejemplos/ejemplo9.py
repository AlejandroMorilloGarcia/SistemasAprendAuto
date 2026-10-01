#muy util * cuando no sabemos de ante mano cuantos valores recibira una funcion
def calcular_promedio(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
print(calcular_promedio(10, 20, 30))
print(calcular_promedio(5, 10, 15, 20, 25))