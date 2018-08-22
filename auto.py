# Autor: Rubén Villalpando Bremont, A01376331, grupo 4
# Descripcion: Programa que le pregunta al usuario la velocidad a la que viaja un auto y le devuelve unos datos específicos.

# Escribe tu programa después de esta línea
velocidad = int(input("Escriba la velocidad a la que va un vehículo en km/h: "))
distancia_7horas = velocidad*7
distanciaCuatroHorasYMedia = velocidad*4.5
tiempoQueTarda = 791/velocidad

print("La distancia recorrida en 7 horas es: ", distancia_7horas, "km")
print("La distancia recorrida en 4.5 horas es: ", distanciaCuatroHorasYMedia, "km")
print("El tiempo que se tarda en recorrer 791km. es de ", tiempoQueTarda, "horas")

