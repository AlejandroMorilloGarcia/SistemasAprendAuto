print("------Asignaturas optativas------")

print("Optativas: Informatica gráfica - Pruebas de software - Usabilidad.")

opcion = input("Escribe la asignatura a elegir: ")

asignatura = opcion.lower()

if asignatura in ("informatica gráfica, pruebas de software, usabilidad y accesibilidad"):
    print("Asignatira elegida: " + asignatura)
else:
    print("La asignatura elegida no se contempla")