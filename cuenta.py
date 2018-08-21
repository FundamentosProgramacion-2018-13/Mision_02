# Autor: David Rodriguez Fragoso, A01748760
# Descripcion: Problema 3
# Escribe tu programa después de esta línea.

#Propina = 13%
#IVA = 15%

comida = int(input("Costo de su comida: "))
propina = comida*0.13
iva = comida*0.15
total = comida+propina+iva

print ("Costo de su comida: $%4.3f"% (comida))
print ("Propina: $%4.3f"% (propina))
print ("IVA: $%4.3f"% (iva))
print ("Total a pagar: $%4.3f"% (total))
