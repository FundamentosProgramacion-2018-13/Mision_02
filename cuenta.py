# Autor: Mariana Caballero Cabrera, A01376544
# Descripcion: A continuación haré un programa que pregunte al usuario el precio de su comida y le calcule cuanto va a pagar de IVA y propina para sacar su total

# Escribe tu programa después de esta línea.

subTotal = float (input("Costo de su comida: "))

iva = subTotal*.15
propina = subTotal*.13
total = subTotal + iva + propina

print ("IVA $ %5.2f" % (iva))
print ("Propina $ %5.2f"  %(propina))
print (" Su total es de $ %5.2f" %(total))
