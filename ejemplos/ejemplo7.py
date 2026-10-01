#Funciones
def mensaje():
    print("Aqui ponemos la sentencia uno")
    print("Aqui ponemos la sentencia dos")
    print("Aqui ponemos la sentencia tres")

#primera llamada
mensaje()

print("------------------------------------")
#segunda llamada
mensaje()

print("------------------------------------")
def suma(num1,num2):
    resultado = num1+num2
    return resultado

almacen_resultado = suma(56,87)
print(almacen_resultado)