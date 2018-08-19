# Autor: Sebastian Macias Ibarra, A01376492
# Descripcion: Obtener la propina, el IVA y el total a pagar.

# Escribe tu programa después de esta línea.
costoComida= int(input("Costo de la comida: $"))

propina = costoComida * 0.13
IVA = costoComida * 0.15
total = costoComida + IVA + propina

print("Propina: $", format(propina, ".2f"))
print("IVA: $", format(IVA, ".2f"))
print("Total a pagar: $", format(total, ".2f"))
