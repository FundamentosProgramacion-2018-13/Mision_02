# Autor: Sebastian Macias Ibarra, A01376492
# Descripcion: Calcular la distancia entre coordenadas

# Escribe tu programa después de esta línea.
x1 = int(input("Escribe x1: "))
x2 = int(input("Escribe x2: "))
y1 = int(input("Escribe y1: "))
y2 = int(input("Escribe y2: "))

x = (x2 - x1)**2
y = (y2 - y1)**2
distancia = (x + y)**0.5

print ("Distancia: %.4f" % distancia)
