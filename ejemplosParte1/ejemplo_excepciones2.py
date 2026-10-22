def divide():
    try:
        
        op1 = (int(input("Introduce el primer numero: ")))
        op2 = (int(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))
    except ValueError:
        print("El valor introdicido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Calculo finalizado")

divide()