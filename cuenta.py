# Autor: Ivan Honc Ayón, A01376466
# Descripcion: Este programa sirve para calcular el total de una cuenta de restaurante.

# Escribe tu programa después de esta línea.

comida = float(input("Escribe el precio de la comida: "))

subtotal = comida
propina = comida*0.13
iva = comida*0.15
total = subtotal + propina + iva

print("""
El precio de la comida es: $%5.2f
La propina es de: $%5.2f
El IVA es de: $%5.2f
El total a pagar es de: $%5.2f""" % (subtotal, propina, iva, total))
