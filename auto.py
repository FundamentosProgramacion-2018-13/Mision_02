#Autor: Alex Serrano Durán, A01376364
#Descripcion: Este programa calcula distancias y tiempos que toma un coche a partir de una velocidad

v = float(input("¿A qué velocidad va el coche (en km/h? "))

d1=v*7
d2=v*4.5
t=791/v

print("""Distancia recorrida en 7 horas: %.1f km
Distancia recorrida en 4.5 horas: %.1f km
Timepo para recorrer 791 km: %.1f hrs.""" % (d1, d2, t))
