# Autor: Javier Alexandro Vargas Sánchez, A01377718
# Descripcion: Este programa obtiene distancias y tiempo establecidos si le introduces una velocidad de km/horas.

# Escribe tu programa después de esta línea.
velocidad =(int(input("Introduzca la velocidad del auto: ")))


distancia1 = velocidad *7
distancia2 = velocidad * 4.5

tiempoEnDist = 791 / velocidad

print("Siendo la velocidad del auto de:  ", velocidad, " kilómetros por hora")
print("La distancia adquirida en 7 horas sería de:  ", distancia1, "km")
print("La distancia adquirida en 4.5 horas sería de:  ", distancia2, "km")
print("Recorreriamos 791 km en un tiempo de:   ", format(tiempoEnDist, ".4f"), "horas")

