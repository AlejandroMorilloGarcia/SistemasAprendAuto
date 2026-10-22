#Tuplas 2

mitupla = ("Antonio", 30, 1, 1995)
mituplados = "Mercedes", 30, 1, 1995
milista = list(mitupla) #convertir la tupla en lista

# milista = ["Laura", 20, 4, 1997]
# mitupla = tuple(milista) convierte la lista en tupla
# print(mitupla)

print(mitupla[2])
print(milista)
print("Antionio" in mitupla) # se enecuentra dentro de la tupla
print(mitupla.count(30)) #Cuentas veces tiene algo concreto
print(len(mitupla)) #Numero de elementos

nombre, dia, mes, agno = mitupla #desempaquetado de tuplas
print(nombre)
print(dia)
print(mes)
print(agno)