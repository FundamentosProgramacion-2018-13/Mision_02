# Autor: Alex Fernando Leyva Martínez, A01747078
# Descripcion: Determinar distancia y tiempo de los problemas usando los datos dados.

# Escribe tu programa después de esta línea.
velocidad = float(input("Velocidad: "))
tiempoA = float(7.00)
tiempoB = float(4.50)
distancia = float(791.00)

distancia1 = (velocidad*tiempoA)
distancia2 = (velocidad*tiempoB)
tiempo = (distancia/velocidad)


print("velocidad del auto en km/h: ", velocidad)
print("Distancia recorrida en 7 hrs. : ", distancia1,"km")
print("Distancia recorrida en 4.5 hrs. : ", distancia2, "km")
print("Tiempo para recorrer 791 km.: %.4f" % tiempo, "hrs")
