class Persona():
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Residencia: {self.lugarResidencia}")

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} Antigüedad: {self.antiguedad}")

antonio = Empleado(1500, 15, "Antonio", 55, "España")
antonio.descripcion()
print("--------------------------------")
manuel = Persona("Manuel", 60, "España")
manuel.descripcion()
print("--------------------------------")
print(isinstance(antonio, Empleado))
print(isinstance(antonio, Persona))
print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))
