# Autor: Humberto Carrillo Gómez, A01377246
# Descripcion: Este programa calcula el total a pagar de una cuenta considerando el Iva y la propina.

# Escribe tu programa después de esta línea.

costoComida=int(input("Teclee el precio de su comida "))
propina= costoComida*0.13
iva=costoComida*0.15
total= costoComida+ propina+ iva

print("Costo de la comida: ",costoComida)
print("Propina: ",format(propina,".2f"))        # Incluir centavos
print("IVA:",format(iva,".2f"))
print("Total a pagar",format(total,".2f"))
