# Autor: Samantha Martínez Franco, A01747686
# Descripcion: Calcular distancia entre dos puntos de coordenadas

# Escribe tu programa después de esta línea.

x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))

distancia=((x2-x1)**2+(y2-y1)**2)**0.5

print("distancia: %5.4f" % (distancia))