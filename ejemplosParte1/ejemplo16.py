#Diccionarios

dicc = {"red":"rojo", "blue":"azul", "green":"verde"}
dicc["black"] = "negro"
dicc.pop("blue")
#tambien borramos con dicc.del(dicc"blue)
print(dicc)
print(dicc["red"])
for key in dicc:
    print(key, "->", dicc[key])
