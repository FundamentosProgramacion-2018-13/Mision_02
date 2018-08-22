# Autor: Joshua Sánchez Martínez, A01274269
# Descripcion: Proporcionar el costo total de una comida.

# Escribe tu programa después de esta línea.

costo = float(input("Teclea el costo de la comida: "))

propina = (13*costo)/100
iva = (15*costo)/100
total = costo + propina + iva
print("costo de su comida: $ %.2f" % costo)
print("propina: $ %.2f " % propina)
print("iva: $ %.2f" % iva)
print("total a pagar: $ %.2f" % total)