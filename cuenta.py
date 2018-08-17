# Autor: Samantha Martínez Franco, A01747686
# Descripcion: Calcular la cuenta total a pagar, calculando IVA y propina

# Escribe tu programa después de esta línea.

costo=int(input("¿Cuánto costó la comida?"))

iva=costo*.15
propina=costo*.13
total=costo+iva+propina

print("Costo de la comida: ", costo)
print("Propina: $%5.2f" % (propina))
print("IVA: $%5.2f" % (iva))
print("Total a pagar: $%5.2f"% (total))