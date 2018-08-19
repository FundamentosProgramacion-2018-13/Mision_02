# Autor: Irma Gómez Carmona, A01747743
# Descripcion: El usuario especifica las coordenadas de los dos puntos para poder calcular la distancia entre ellas 
# Escribe tu programa después de esta línea.


import math

x1=int(input("X1= "))
y1=int(input("Y1= "))
x2=int(input("X2= "))
y2=int(input("Y2= "))

radicando= (x2-x1)**2+(y2-y1)**2
distancia= math.sqrt(radicando)

print("Dsitancia: %.4f"%(distancia))
