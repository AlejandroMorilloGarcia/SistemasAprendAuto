#Condicionales

a = 10
b = 20
if (a>b):
    print(f"El número mayor es {a}")
elif(b>a):
    print(f"El número mayor es {b}")
else:
    print(f"Los dos numeros son iguales")

print("---------------------------------------")
#Condicionales 2
print("Programa evaluación de notas")

nota_alumno = input("Introduce la nota de alumno: ")

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion
print(evaluacion(int(nota_alumno)))