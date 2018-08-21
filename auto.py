# Autor: Ivan Honc Ayón, A01376466
# Descripcion: Este programa calcula distancias y tiempos específicos a partir de una velocidad dada.

# Escribe tu programa después de esta línea.

velocidad = float(input("Escribe la velocidad que requieres para hacer los cálculos: "))

distancia1 = velocidad*7
distancia2 = velocidad*4.5
tiempo1 = 791.00/velocidad

print("""
Tu velocidad es: %d
Tu distancia recorrida después de 7 horas es de: %5.2f
Tu distancia recorrida después de 4.5 horas es de: %5.2f
El tiempo necesario para recorrer 791km a esta velocidad es de: %5.2f""" % (velocidad, distancia1, distancia2, tiempo1))
