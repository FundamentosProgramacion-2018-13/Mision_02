# Autor:Oscar Macias Rodríguez, A01376398
# Descripción: Calcule la distancia entre dos puntos.


x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distancia:", "%.4f" % d)