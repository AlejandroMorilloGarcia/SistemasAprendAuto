# nos devuelve una lista de 5 elementos: 0,1,2,3,4
for i in range(5):
    print(i)

#f notacion especial. concatena el texto con el valor de la variable en cada vuelta del bucle

for i in range(5):
    print(f"valor variable {i}")

#empieza en 5, termina en 50, avanza de 3 en 3. probar 2 parametros
for i in range(5,50,3):
    print(f"Valor de la variable {i}")

valido = False
email = input("introduce el email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

citricos = ["limon", "naranja", "pomelo", "lima"]

for fruta in citricos:
    print(fruta)
for numero in range(3):
    print(f"Numero: {numero}")
for numero in range(len(citricos)):
    print(f"P: {numero} - V: {citricos[numero]}")