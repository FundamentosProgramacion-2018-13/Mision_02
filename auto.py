# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
Vel = input("Velocidad del auto en km/h: ")
velocidad = float(Vel)

distancia1 = velocidad * 7
distancia2 = velocidad * 4.5
tiempo = 791 / velocidad

print("Distancia recorrida en 7 hrs: ", distancia1, " km")
print("Distancia recorrida en 4.5 hrs: ", distancia2, " km")
print("Tiempo para recorrer 791 km: ", tiempo , " hrs")
