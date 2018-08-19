#Autor: Alex Serrano Durán, A01376364
#Descripcion: Este programa le da al usuario su total a pagar (incluyendo propina e IVA) para una comida.

subtotal = float(input("Costo de la comida: "))

propina = subtotal*0.13
iva = subtotal * 0.15
total = subtotal+propina+iva

print("""
Propina: %.2f
IVA: %.2f
Total a pagar: %.2f""" % (propina, iva, total))
