# Diccionarios 2

midiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"] = "Lisboa"

print(midiccionario["España"]) #Valor Madrid
print(midiccionario)

midiccionario["Italia"] = "Roma"
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

print("---------------------------")

mitupla = ["España", "Francia", "Alemania", "Reino Unido"]
midiccionariodos = {mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Berlín", mitupla[3]:"Londres"}
print(midiccionariodos)

#Tupla dentro de diccionario
#midiccionario = {23:"Jordan", "nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":[1991,1992,1993,1996,1997,1998]}
#print(midiccionario)
#print(midiccionario("Anillos"))

# Diccionario diccionario y tuplas
#midiccionario = {23:"Jordan", "nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":["Temporadas":[1991,1992,1993,1996,1997,1998]]}