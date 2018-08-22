# Autor: Luis Armando Miranda Alcocer, A01377115
# Descripcion: Dado el costo de la comida, se calcula la propina (13%), el IVA (15%), y el costo total.

# Escribe tu programa después de esta línea.

costo = float(input( "¿Cuál es el costo de su comida?: "))
print ("Costo de la comida: ", '%.2f' % costo)
prop = costo * 0.13
print ("Propina: ", '%.2f' % prop)
iva = costo * 0.15
print ("IVA: ", '%.2f' % iva)
total = costo + prop + iva
print ("Total a pagar: ", '%.2f' % total)
