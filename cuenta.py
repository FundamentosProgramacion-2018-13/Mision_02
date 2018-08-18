# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

totalComida = int(input ("¿Cuánto fue en total? "))
print ("Su subtotal es: ", str(totalComida))
propina = totalComida * .13
print ("El monto de propia es ", str(propina))
iva = totalComida * .15
print ("El monto de iva es: ", str(iva))
precioPagar = totalComida + propina + iva
print ("Su cuenta total es: ", str(precioPagar))
