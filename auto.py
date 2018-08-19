# Autor: Sebastian Macias Ibarra, A01376492
# Descripcion: Sacar los kilómetros recorridos para 7 y 4.5 horas y el tiempo para 791 km

# Escribe tu programa después de esta línea.
velocidad = int (input ("Escribe la velocidad del auto en km/h: "))

distancia1 = velocidad * 7
distancia2 = velocidad * 4.5
tiempo = 791 / velocidad

print(" ")
print("Distancia recorrida por el auto en 7 h: ", distancia1, "km")
print("Distancia recorrida por el auto en 4.5 h: ", distancia2, "km")
print("Tiempo necesario para recorrer 791 km: ", format(tiempo, ".1f"), "horas")
