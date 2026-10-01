def saluda(nombre):
    print(f"Hola {nombre} !!!")
def suma(a,b):
    return(a+b)
def addColor(colores, color):
    colores.append(color)
    return True
saluda("Borja")
print(suma(10,20))
colores = ["azul", "rojo", "verde"]
addColor(colores, "negro")
print(colores)