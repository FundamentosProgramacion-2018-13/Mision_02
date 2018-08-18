# Autor: alejandroToricesOliva, A01377744
# Descripcion: cuenta de un restaurante con propina, IVA, total

# Escribe tu programa después de esta línea.
costo = float(input("Introduzca el costo de la comida: "))

propina = costo * .13
IVA = costo * .15
total = costo + propina + IVA

print("Costo de su comida: $%3.2f" % costo)
print("Propina: $%3.2f" % propina)
print("IVA: $%3.2f" % IVA)
print("Total a pagar: $%3.2f" % total)
