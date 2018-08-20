# Autor: Irma Gómez Carmona, A01747743
# Descripcion: Se debe saber cuanto es el total que se va a pagar por la comida, agregando el iva (15%) y la propina (15%)

# Escribe tu programa después de esta línea.

costoi=float(input("Costo de su comida: "))
propina=costoi*0.13
iva=costoi*0.15
total=costoi+propina+iva

print ("Propina: $%.2f"%(propina))
print ("IVA: $%.2f"%(iva))
print ("Total a pagar: $%.2f"%(total))
