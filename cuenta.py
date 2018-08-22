# Autor: María Fenanda Vela Calderón, A01377958
# Descripcion: Calcular distancia y tiempo que viaja el auto

# Escribe tu programa después de esta línea.

costo = int( input( "Escribe el costo de la comida: "))

propina = costo*0.13

iva = costo*0.15

total = costo + propina + iva

print( "Costo de su cominda: $ %9.02f" % costo)
print( "Propina: $ %9.02f" % propina)
print( "IVA: $ %9.02f" % iva)
print( "Total a pagar: $ %9.02f" % total)
