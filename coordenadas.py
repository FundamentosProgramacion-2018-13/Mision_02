# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula la distancia entre dos puntos
"""
Análisis:
E:x1,y1,x2,y2
S:distancia
E/S:
distancia=raiz ((x2-x1)**2+(y2-y1)**2)

Algoritmo:
Obtener variables x1, x2, y1 y y2 del usuario y asigarlos
Restar los 1 de los 2
Elevar el cuadrado los resultados
Sumarlos y elevarlos a 0.5
Reportar resultado
"""

X1 = float(input("X1:"))
Y1 = float(input("Y1:"))
X2 = float(input("X2:"))
Y2 = float(input("Y2:"))
total = ((X2-X1)**2)+((Y2-Y1)**2)
total = total ** 0.5
print("X1: " + X1)
print("Y1: " + Y1)
print("X2: " + X2)
print("Y2: " + Y2)
print("Distancia entre los puntos: " + "{:,.4f}%".format(total))
