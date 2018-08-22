# Autor: Joshua Sánchez Martínez, A01274269
# Descripcion: Calcular distancia entre dos puntos dadas las cordenadas.

# Escribe tu programa después de esta línea.

x1 = int(input("Teclea la cordenada x del punto 1: "))
y1 = int(input("Teclea la cordenada y del punto 1: "))
x2 = int(input("Teclea la cordenada x del punto 2: "))
y2 = int(input("Teclea la cordenada y del punto 2: "))

distancia = (((x2-x1)**2)+((y2-y1)**2))**0.5

print("distancia entre los dos puntos: %.4f" % distancia)