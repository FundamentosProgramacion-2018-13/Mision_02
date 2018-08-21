# Autor: Alex Fernando Leyva Martínez, A01747078
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Determinar, el IVA, propina y el total utilizando el valor del total de la comida.

# Escribe tu programa después de esta línea.
totalNeto = float(input("Costo de su comida: "))

propina = float(totalNeto * .13)
iva = float (totalNeto * .15)
total = (totalNeto + propina + iva)

print("Costo de su comida: $%.2f"% totalNeto)
print("Propina: $%.2f" % propina)
print("IVA: $%.2f" % iva)
print("Total a pagar: $ %.2f " % total)
