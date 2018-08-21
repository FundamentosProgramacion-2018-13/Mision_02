costo = int(input("Costo de su comida: "))

prop = costo*0.13
iva = costo*0.15
total = costo + prop + iva


print("Propina: $",prop)
print("IVA: $",iva)
print("Total a pagar : $",total)
