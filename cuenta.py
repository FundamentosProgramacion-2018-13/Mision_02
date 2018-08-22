# Autor: Juan Carlos Flores García, A01376511
# Descripcion: Programa que calcula la propina, iva y total a pagar.

# Escribe tu programa después de esta línea.
totalComida = int(input("Introduzca el precio de su comida: "))

propina = totalComida*.13

iva = totalComida*.15

totalAPagar = totalComida + propina + iva

print("Costo de su comida: ", totalComida)
print("Propina: $ %.2f" % propina)
print("IVA: $ %.2f" % iva)
print("Total a pagar: $ %.2f" % totalAPagar) 
