costoComida = int(input("Introduzca el costo de su comida: "))
propina = costoComida * 0.13
iva = costoComida * 0.15
total = costoComida + propina + iva
print("Costo de su comida: ", costoComida)
print("Propina: %.02f" % propina)
print("IVA: %.02f" % iva)
print("Total a Pagar: %.02f" % total)