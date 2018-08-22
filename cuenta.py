# Autor: Carlos Badillo García, A01377618
# Descripcion: Calcular el total a pagar de una comida añadiendo la propina y el IVA al costo.

# Escribe tu programa después de esta línea.

tc = int(input("¿Cual fue el costo de la comida?"))
pro = tc*.13
iva = tc*.15
tapagar = tc + (tc*.13) + (tc*.15)

print("Lo que se pago solo por la comida fueron: $", tc)
print("La propina proporcionada fue de: $", pro)
print("El IVA es de: $", iva)
print("El total a pagar por toda la comida fue de: $", tapagar)
