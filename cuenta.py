# Autor: Alek Fernando Howland Aguilar, A01747765
# Descripcion: Unprograma que calcula el costo total de una comida en un restaurante.

# Escribe tu programa después de esta línea.

print ("Bienvenido")
print("..............")

subtotal = float(input("Cual fue el total de la cuenta:"))

prop = 13*subtotal/100
iva = 15*subtotal/100
total = subtotal+prop+iva

print("..............")

print ("Subtotal de:", subtotal)
print ("Fueron de IVA:%.2f" % (iva))
print ("Fue de propina: %.2f" % (prop))
print ("Total de: %.2f" % (total))
print("..............")

print ("Gracias")




