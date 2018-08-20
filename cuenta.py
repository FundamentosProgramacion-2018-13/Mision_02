# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Programa que calcula el costo total de una comida en un restaurante

# Escribe tu programa después de esta línea.

tot_par = int(input("¿Cuál fue el total de su comida? "))

iva = tot_par * .15
prop = tot_par * .13
tot_fin = tot_par + iva + prop

print("Subtotal: $", tot_par)
print("IVA: $ %.2f" % iva)
print("Propina: $ %.2f" % prop)
print("Total: $", tot_fin)
