#Parametros por nombre
def resta(a,b):
    return a-b

print(resta(b=30, a=10))
print("----------------------")
#parametros por defecto
def resta(a=None, b=None):
    if (a == None or b == None):
        print("Error, debes enviar dos numeros a la funcion")
        return
    return a - b
resta(30-10)
resta()
print("----------------------")
#parametros por indeterminados, args es una tupla
def indeterminados(*args):
    for arg in args:
        print(arg)

indeterminados(5, "Hola Plone", [1,2,3,4,5])
print("----------------------")
#parametros po indeterminados, kwargs es un diccionario
def indeterminados(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados(n=5, c="Hola Plone", l=[1,2,3,4,5])