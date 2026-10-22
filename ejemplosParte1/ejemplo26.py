#generadores
def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num = num + 1

devuelvePares = generaPares(10)

print(next(devuelvePares))
print("------------------")
print(next(devuelvePares))
print("------------------")
print(next(devuelvePares))
print("------------------")
print(next(devuelvePares))

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Zamora", "Valladalodid", "Cuenca")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
