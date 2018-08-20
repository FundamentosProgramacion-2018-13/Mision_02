# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

x1 = int(input("¿Cuáles son las coordenadas x del punto 1? "))
y1 = int(input("¿Cuáles son las coordenadas y del punto 1? "))
x2 = int(input("¿Cuáles son las coordenadas x del punto 2? "))
y2 = int(input("¿Cuáles son las coordenadas y del punto 2? "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**.5

print("La distancia entre los dos puntos es: %.2f" % d)