# Autor: Zoe Caballero Dominguez, A01747247
# Descripcion: Dada la velocidad por el usuario, se calcula cuanta distancia es recorrida en 7 y 4.5 horas; y el tiempo que lleva recorrer 791Km

# Escribe tu programa después de esta línea.
velocidad = int(input("Velocidad del auto en km/h:"))
primeraDistancia = float(velocidad * 7)
segundaDistancia = float(velocidad * 4.5)
tiempo = float(791/velocidad)
print ("Distancia recorrida en 7 hrs: %.1f km" % (primeraDistancia))
print ("Distancia recorrida en 4.5 hrs: %.1f km" % (segundaDistancia))
print ("Tiempo para recorrer 791 km: %.1f hrs" % (tiempo))
