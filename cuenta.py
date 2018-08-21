# Autor: Zoe Caballero Dominguez, A01747247
# Descripcion: Se escribe el costo de la comida y se calcula el iva, la propina y el costo total

# Escribe tu programa después de esta línea.
subtotal = int(input("Costo de su comida:"))
iva = subtotal * 0.15
propina = subtotal * 0.13
costoTotal = subtotal + propina + iva
print ("Propina: $%.2f" % (propina))
print ("IVA: $%.2f" % (iva))
print ("Total a pagar: $%.2f" % (costoTotal))
