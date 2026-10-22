#Bucles For

contEmail1 = 0
contPunto = 0
miEmail = input("Introduce tu email: ")

for i in miEmail:
    if (i == "@"):
        contEmail1 = contEmail1 + 1
    elif (i == "."):
        contPunto = contPunto + 1

if (contEmail1 == 1 and (contPunto >= 1 and contPunto <=4)):
    print("El email es correcto")
else:
    print("El email no es correcto")