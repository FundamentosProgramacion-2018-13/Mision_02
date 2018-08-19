# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

costoi=float(input("Costo de su comida: "))
propina=costoi*0.13
iva=costoi*0.15
total=costoi+propina+iva

print ("Propina: $%.2f"%(propina))
print ("IVA: $%.2f"%(iva))
print ("Total a pagar: $%.2f"%(total))
