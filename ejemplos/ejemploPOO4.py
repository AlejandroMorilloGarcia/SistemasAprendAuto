#Herencia Multiple
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrena {self.frena}")

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "voy a hacer un caballito"

    def estado(self):
            print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrena {self.frena} \n {self.hcaballito}")

class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargaElectrica(self):
        self.cargando = True

class BicicletaElectrica(VElectricos, Vehiculos): #herencia multiple se le da prioridad al primer contructor    
    pass

miMoto = Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica()