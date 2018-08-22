# Autor: Rubén Villalpando Bremont, A01376331, grupo 4
# Descripcion: El usuario ingresa el costo de la comida y el programa le muestra el iva, la propina, y el total a pagar.

# Escribe tu programa después de esta línea.
totalComida = int(input("Escriba el total de su comida: "))
propina = totalComida*0.13
iva = totalComida*0.15
total_a_Pagar = totalComida + propina + iva
print("Propina: $", propina)
print("IVA: $", iva)
print("Total a pagar: $", total_a_Pagar)
