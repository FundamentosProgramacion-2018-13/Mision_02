# Autor: luisJonathanRosasRamos, A01377042
# Descripcion: Obtener la distacia con una velocidad de 115 en el tiempo de 7, 4.5 y el tiempo necesario para recorrer una cantidad de kilometros

# Escribe tu programa después de esta línea.

v = float(input("Cual fue la velocidad: "))


print("Velocidad del auto en Km/h:", v)
d = v*7
print("Distancia recorrida en 7 hrs: ", d, "Km")
di = v+4.5
print("Distancia recorrida en 4.5 hrs: " ,di, "Km")
t = 791/v
print("Tiempo para recorrer 791 km: %5.4f" %(t),"hrs")
