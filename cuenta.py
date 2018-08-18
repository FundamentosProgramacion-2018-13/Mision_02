# Autor: Saúl Figueroa Conde, A01747306
# Descripcion: Calcula el subtotal, propina, IVA y valor total de una comida.

# Escribe tu programa después de esta línea.

costo = input("Escriba el costo de su comida: ")

propina = float(costo)*0.13
iva = float(costo)*0.15
total = float(costo) + propina + iva



print("Costo de su comida: ", costo,)
print ("Propina: ", "%.2f"% propina)
print("IVA: ", "%.2f"% iva)
print("Total a pagar: ", "%.2f"% total)