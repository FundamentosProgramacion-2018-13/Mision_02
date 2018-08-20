# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Programa que calcula la distancia y tiempo basado en la velocidad de un auto
# Escribe tu programa después de esta línea.

v = int(input("¿A qué velocidad viaja el auto? (km/h) "))

d1 = v * 7
d2 = v * 4.5

t = 791/v

print("En 7 horas el coche recorre", d1,"km")
print("En 4.5 horas el coche recorre", d2,"km")
print("A",v,"km/h, el coche tardará", t,"horas en recorrer 791 km")