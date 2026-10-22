#Bucles While

i = 1
while i <=10:
    print("Ejecucion " + str(i))
    i = i + 1
print("termino sisi")

edad = int(input("introduce tu edad: "))

while edad < 5 or edad > 100:
    print("has introducico una edad erronea. vuelve a intentarlo pelotudo")
    edad = int(input("introduce tu edad: "))

print("Gracias")
print("edad del usuario: " + str(edad))

#Programa que averigue la raiz cuadrada de un numero, incluye importar.
import math

print("----programa de calculo de raiz cuadrada----")
numero = int(input("introduce un numero: "))

intentos = 0

while numero < 0:
    print("no se puede hallar la raiz de un numero negativo.")

    if intentos == 2:
        print("has consumido demasiados intentos")
        print("el programa ha finalizado")
        break
    numero = int(input("introdice un numero: "))

    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es: " + str(solucion))