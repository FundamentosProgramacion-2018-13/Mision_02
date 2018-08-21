# Alek Fernando Howland Aguilar, A01747765
# Un programa que calcula la distancia entre dos puntos.

print ("Bienvenido")

print ("..............")

x1 = float(input("Ingresa las coordenada para x1: "))
y1 = float(input("Ingresa las coordenada para y1: "))
x2 = float(input("Ingresa las coordenada para x2: "))
y2 = float(input("Ingresa las coordenada para y2: "))

distancia1 = (x2 - x1) ** 2
distancia2 = (y2 - y1) ** 2
distancia_total = (distancia1 + distancia2) ** 0.5

print ("..............")

print ("Distancia: %.4f " % (distancia_total))

print ("..............")
