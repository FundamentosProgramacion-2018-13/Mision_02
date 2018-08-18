# Autor: Silvia Ferman Muñoz, A01376718
# Descripcion: Calcular el costo TOTAL de una comida

# Escribe tu programa después de esta línea.

tcomida = int(input("Cual es el total de la comida:"))
p = tcomida * 0.13
iva = tcomida * 0.15
T = tcomida + p + iva

print("El subtotal es:", tcomida)
print("La propina es: %.2f" % p)
print("El IVA es: %.2f" % iva)
print("El Total a pagar es: %.2f" % T)
