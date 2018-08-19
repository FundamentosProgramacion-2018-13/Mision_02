# Autor: Víctor Manuel Rodríguez Loyola, A01747755
# Descripcion: Este programa calcula el total a pagar de una persona en un restaurante,
# considerando la propina e IVA correspondiente.

# Escribe tu programa después de esta línea.

totalcomida= int(input("Escribe el costo total de tu comida "))
iva= (totalcomida*.15)
propina= totalcomida*.13
pagototal=totalcomida+iva+propina

print("Costo de su comida: $%.2f" % totalcomida)
print("Propina: $%.2f" % propina)
print("IVA: $%.2f" % iva)
print("Total a pagar: $%.2f" % pagototal)


