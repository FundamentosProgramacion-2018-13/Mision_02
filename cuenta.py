# Autor: Sebastian Macias Ibarra, A01376492
# Descripcion: Obtener la propina, el IVA y el total a pagar.

# Escribe tu programa después de esta línea.
costoComida= int(input("Costo de la comida: $"))

propina = costoComida * 0.13
IVA = costoComida * 0.15
total = costoComida + IVA + propina

print("Costo de su comida: $", costoComida)
print("Propina: $", propina)
print("IVA: $", IVA)
print("Total a pagar: $", total)
