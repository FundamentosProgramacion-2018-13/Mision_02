# Autor: Ivan Honc Ayón, A01376466
# Descripcion: Este programa calcula distancias y tiempos específicos a partir de una velocidad dada.

# Escribe tu programa después de esta línea.

x1 = float(input("Escriba la coordenada de x1: "))
y1 = float(input("Escriba la coordenada de y1: "))
x2 = float(input("Escriba la coordenada de x2: "))
y2 = float(input("Escriba la coordenada de y2: "))

distancia = (((x2-x1)**2)+((y2-y1)**2))**(1/2)

print("la distancia entre los dos puntos dados es: %5.4f" % distancia)