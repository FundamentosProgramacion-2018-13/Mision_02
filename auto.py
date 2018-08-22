# Autor: Joshua Sánchez Martínez, A01274269
# Descripcion: Leer velocidad y calcular tres resultados.

# Escribe tu programa después de esta línea.


velocidad = float(input("Teclea la velocidad del auto: "))

d7 = velocidad*7
d45 = velocidad*4.5
tr791 = 791/velocidad


print("distancia recorrida en 7 hrs: %.1f" % d7, "km")
print("distancia recorrida en 4.5 hrs: %.1f" % d45, "km")
print("tiempo para recorrer 791 km: %.1f" % tr791, ("hrs") )