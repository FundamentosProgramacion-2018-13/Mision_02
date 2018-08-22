# Autor: Jocelyn López Ortíz A01377451
# Descripcion: Cálculo de la distancai recorrida pro un auto en 4.5 y 7 horas con respecto a una velocidad dada así como el tiempo que toma el auto en recorrer 791km

# Escribe tu programa después de esta línea.
velocidad = int(input("Velocidad del auto en km/h: "))

distancia1 = velocidad*7
print("Distancia recorrida en 7 hrs: ", distancia1, "km")

distancia2 = velocidad*4.5
print("Velocidad del auto en km/h: ", distancia2, "km")

tiempo791 = 791/velocidad
print("Tiempo para recorrer 791 km: ", round(tiempo791,4) , "horas")
