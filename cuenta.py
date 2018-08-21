# Autor: Diana Marisol Medina Bravo, A01748753
# Descripcion: Se calcula el total a pagar con la suma del porcentaje de propina, el porcentaje de iva y el costo inicial de la comida

# Escribe tu programa después de esta línea.

costoComida=int(input("Introduzca el costo de la comida:"))

propina=costoComida*0.13
iva=costoComida*0.15
totalAPagar= costoComida+propina+iva

print("Propina es:$%5.2f" % propina)
print("IVA:$%5.2f" % iva)
print("El total a pagar es:$%5.2f" % totalAPagar)
