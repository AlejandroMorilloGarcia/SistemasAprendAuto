def calcular_precio_final(precio, iva=0.21):
    return precio * (1+iva)
precio = calcular_precio_final(100)
print(precio)
precio_reducido = calcular_precio_final(100, 0.10)
print(precio_reducido)