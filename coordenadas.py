#Autor: Saúl Figueroa Conde, A01747306
# Descripcion: Programa que calcula la distancia entre dos puntos.

# Escribe tu programa después de esta línea.

import math

x1 = int(input("indique el valor de la coordenada x1:" ))
y1 = int(input("indique el valor de la coordenada y1:" ))
x2 = int(input("indique el valor de la coordenada x2:" ))
y2 = int(input("indique el valor de la coordenada y2:" ))

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("x1:", x1)
print("y1:", y1)
print("x2:", x2)
print("y2:", y2)
print("Distancia: ", "%.4f"% distancia)