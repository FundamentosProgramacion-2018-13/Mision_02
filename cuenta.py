# Autor: Javier Alexandro Vargas Sánchez, A01377718
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
costoComida= (int(input("Teclea el subtotal de tu comida:  ")))


propina = costoComida*.13

iva = costoComida *.15

costoTotal = propina + iva +costoComida

print("El subtotal fue: ", costoComida)
print("El Iva fue de:  ", iva)
print ("Dejaste esta cantidad de propina:  ", propina)
print ("El costo total de tu comida fue de: ", costoTotal)
