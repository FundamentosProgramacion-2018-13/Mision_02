# Autor: Irma Gómez Carmona, A01747743
# Descripcion: Dependiendo de la velocidad de un auto, se debe calcular que distancia recorrerá en 7 y 4.5 horas
# y el tiempo que tardará en recorrer 791 km.

# Escribe tu programa después de esta línea.

velocidad=float(input("Velocidad del vehiculo en km/hr: "))

distancia1=velocidad*7
distancia2=velocidad*4.5
tiempo= 791/velocidad

print ("Distancia que recorrera en 7 horas: %.1f" %(distancia1))
print ("Distancia que recorrera en 4.5 horas: %.1f" % (distancia2))
print ("Tiempo que tardará en recorrer 791 km: %.1f" %(tiempo))
