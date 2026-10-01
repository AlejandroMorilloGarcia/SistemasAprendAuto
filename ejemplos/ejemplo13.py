#listas 2

milista = ["Antonio", "Ana", "Federico", "Mercedes"]
milistaDos = ["Alberto", 22, 33, 56, True]
milistaTres = milista + milistaDos
print(milistaTres)

#agregar al final
milista.append("Sandra")

#agregar indice determinado
milista.insert(2, "Manolo")

#agregar varios elementos a una lista, concatenada
milista.extend(["Laura", "Carlos"])

print(milista[:])
print(milista[2])
print(milista[0:3])
print(milista[:3])
print(milista[1:2])
print(milista[2:])

print(milista.index("Antonio"))

print("Antonio" in milista) #Verdadero o falso

print(milistaDos[3])

milista.remove("Ana")
milista.pop() #Elimina el ultimo elemento
