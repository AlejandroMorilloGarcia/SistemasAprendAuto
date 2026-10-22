class Coche():
    laroChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche  esta parado"

miCoche = Coche()
print("El largo del coche es: ", miCoche.laroChasis)
print("el coche tiene: ", miCoche.ruedas, "ruedas.")
miCoche.arrancar()

print(miCoche.estado())