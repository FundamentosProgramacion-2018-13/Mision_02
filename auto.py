# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcular distancia que se puede recorren en cierto tiempo y tiempo que tarda en recorrer cierta distancia el auto

# Escribe tu programa despues de esta linea.
"""
Analisis:
E:velocidad
S:distancia_en_7_horas, distancia_en_4.5_horas, tiempo para recorrer 791km
E/S:
distancia_en_7_horas=velocidad*7
distancia_en_4.5_horas=velocidad*4.5
tiempo para recorrer 791km=791/velocidad

Analisis:
Obtener velocidad de usuario y asignarlo a su variable
Multiplicar por 7 la velocidad y reportarlo
Multiplicar por 4.5 la velocidad y reportarlo
Dividir 791 entre la velocidad y reportarlo

"""
velocidad = input("Velocidad del automovil en km/h")
velocidad = int(velocidad)
dist_7 = velocidad * 7
print("Distancia recorrida en 7 horas: " + str(dist_7))
dist_4_5 = velocidad * 4.5
print("Distancia recorrida en 4.5 horas: " + str(dist_4_5))
tiempo791 = 791/velocidad
print("Tiempo que toma recorrer 791 km: " + str(tiempo791))
