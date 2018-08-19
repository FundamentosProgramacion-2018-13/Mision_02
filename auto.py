# Autor: Víctor Manuel Rodríguez Loyola, A01747755
# Descripcion: Este problema se encarga de calcular el tiempo y distancia que recorre un coche a partir de su velocidad.

# Escribe tu programa después de esta línea.

velocidad= float(input("Escribe la velocidad en km/h que lleva tu coche  "))

dist_7h= velocidad*7
dist_4h= velocidad*4.5
tiempo_791km= 791/velocidad

print("Velocidad del auto en km/h: %.1f" % (velocidad) )
print("Kilómetros recorridos en 7 hrs: %.1f" % (dist_7h) )
print("Kilómetros recorridos en 4.5 hrs: %.1f" % (dist_4h))
print("Horas necesarias para recorrer 791 km: %.1f" % (tiempo_791km))

