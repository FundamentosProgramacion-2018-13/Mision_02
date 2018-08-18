# Autor: Jesus Zabdiel Sanchez Chavez, A01374964
# Descripcion: Programa que calcula el total a pagar por una cuenta.

# Escribe tu programa después de esta línea.

subtotal = int (input("Teclea el costo total de la comida: "))
propina = subtotal * .13
iva = subtotal * .15
total = subtotal + iva + propina

print ("Costo de la comida: $", subtotal)
print ("Propina: $",propina, "IVA: $",iva)
print ("Total a pagar", total)
