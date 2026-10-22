#fecha y hora
from datetime import datetime
datenow1 = datetime.now().date()
print("Fecha: ", datenow1)
datenow2 = datetime.now()
print("Fecha: ", datenow2)
print("Año: ", datenow2.year)
print("Mes", datenow2.month)
print("Día: ", datenow2.day)
print(f"Hora: {datenow2.hour}:{datenow2.minute}")
#parseo de fecha
fecha = "10-14-2018"
obj = datetime.strptime(fecha, "%m-%d-%Y").date()
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")
#formatear fechas
fecha = datetime.now()
print(fecha.strftime("%A, %d %b %Y")) #A dia completo en texto, a dia acortado en texto, b mes en texto acortado, B mes en texto completo, Y año en numero completo, y año en numero acortado
