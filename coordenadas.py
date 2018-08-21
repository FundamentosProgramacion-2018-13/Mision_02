# Autor: Alex Fernando Leyva Martínez, A01747078
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Determinar la distancia entre dos coordenadas usando una formulas con los valores dados.
# Escribe tu programa después de esta línea.
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia = float(((x2-x1)**2)+((y2-y1)**2))**(1/2)

print ("Distancia: %.4f" % distancia)
