# Autor:Alexys Martín Coate Reyes, A01746998

# Descripcion: Calcular el total a pagar de una cuenta dee restaurante, contando el iva y la propina.

"""Elabora un algoritmo y escribe un programa que calcula el costo total de una comida en un restaurante.
# •	El programa le pregunta al usuario el total de la comida.
# •	Agrega 13% de propina y 15% de IVA.
# •	Cada porcentaje se calcula con respecto al costo de la comida.
# •	Imprime:
# o	El subtotal (costo de la comida)
# o	La propina.
# o	El IVA.
# o	El total a pagar. (Suma del subtotal, la propina y el IVA)"""

# Escribe tu programa después de esta línea.

subtotal = float(input("Ingresa el costo total de la comida: "))

propina = subtotal*.13
iva = subtotal*.15
total = subtotal + iva + propina

print("Subtotal: $%.2f" % (subtotal))
print("Propina: $%.2f" % (propina))
print("IVA: $%.2f" % (iva))
print("Total a pagar: $%.2f" % (total))
