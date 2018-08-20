# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
velocidad = float(input("Velocidad del auto en km/h: "))

distancia1 = velocidad * 7
distancia2 = velocidad * 4.5
tiempo = 791 / velocidad

print("Distancia recorrida en 7 hrs: %.1f km" % (distancia1))
print("Distancia recorrida en 4.5 hrs: %.1f km" % (distancia2))
print("Tiempo para recorrer 791 km: %.4f hrs" % (tiempo))
