# Autor:Oscar Macias Rodríguez, A01376398
# Calcula el costo total de una comida en un restaurante


c = int(input("Costo de su comida:"))
p = c*0.13
iva = c*0.15
total = c+p+iva

print("Propina: $", p)
print("IVA: $", iva)
print("Total a pagar: $", total)