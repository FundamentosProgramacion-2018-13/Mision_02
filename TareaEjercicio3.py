# Autor: Roberto Emmanuel González Muñoz A01376803
# Este programa calcula el costo de una comida en un restaurante.

#El usuario introduce el costo total de su comida
comidaT = int(input("Introdusca el costo total de su comida: "))

# Variables globales
IVA = comidaT*(15/100)
propina = comidaT*(13/100)
pagoTotal = comidaT + IVA+ propina

print("Costo de su comida: $",format(comidaT,".2f"))
print("Propina: $",format(propina,".2f"))
print("IVA: $",format(IVA,".2f"))
print("Total a pagar: $",format(pagoTotal,".2f"))