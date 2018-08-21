# Autor: Zoe Caballero Dominguez, A01747247
# Descripcion: Dada la velocidad por el usuario, se calcula cuanta distancia es recorrida en 7 y 4.5 horas; y el tiempo que lleva recorrer 791Km

# Escribe tu programa después de esta línea.

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))

distancia = ((x2 - x1) ** 2 + (y2 - y1)**2) ** 0.5

print ("Distancia= %.4f" % (distancia))
