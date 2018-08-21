# Autor: Jesús Roberto Herrera Vieyra, A01377230
# Descripcion: Programa para calcular el subtotal, propina, IVA y total de una comida

# Escribe tu programa después de esta línea.
costo = float(input("Costo de la comida: "))

propina= costo*0.13
iva= costo*0.15
costo_total= costo+propina+iva

print("costo: $" "{0:.2f}".format(costo))
print("Propina: $", "{0:.2f}".format(propina))
print("IVA: $", "{0:.2f}".format(iva))
print("Total: $", "{0:.2f}".format(costo_total))
