# Autor: Michelle Sánchez Guerrero, A01376622
# Descripcion: Programa que calcula la distancia entre dos puntos.

# Escribe tu programa después de esta línea.

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Distancia: %.4f" %(distancia))
