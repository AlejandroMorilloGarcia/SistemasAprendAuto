#Excepciones
numero1 = 100
numero2 = 0

try:
    print(numero1/numero2)
except ZeroDivisionError:
    print("error al dividir entre cero")
except:
    print("error.")
else:
    print("la division se calculo correctamente")
finally:
    print("Fin del programa")