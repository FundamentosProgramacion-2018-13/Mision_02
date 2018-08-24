Nombre: Jonathan Sanabria Rocha, A01746763
Descripción: Sacar la distancia entre dos puntos mediante una formula, imprimir distancia.

#
x1=float(input("Dame la coordenada x1: "))
y1=float(input("Dame la coordenada y1: "))
x2=float(input("Dame la coordenada x2: "))
y2=float(input("Dame la coordenada y2: "))
import math
x=(x2-x1)**2
y=(y2-y1)**2
sxy=x+y
distancia=math.sqrt(sxy)
print(x1)
print(y1)
print(x2)
print(y2)
print("Distancia: ",format(distancia,".4f"))
