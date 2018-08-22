# Autor:Alexys Martín Coate Reyes, A01746998
# Descripcion: Calcular la distancia entre 2 puntos dados de un plano.

"""Elabora un algoritmo y escribe un programa que calcula la distancia entre dos puntos.
# •	El programa le pregunta al usuario las coordenadas (x1, y1) del primer punto y, también, las coordenadas (x2, y2) del segundo punto.
# •	Imprime:
# o	La distancia entre los dos puntos.
"""

# Escribe tu programa después de esta línea.

x1 = float(input("Inserta el valor de x1: "))
x2 = float(input("Inserta el valor de x2: "))
y1 = float(input("Inserta el valor de y1: "))
y2 = float(input("Inserta el valor de y2: "))

distancia = float(((x2-x1)**2 + (y2-y1)**2)**(1/2))

print("Distancia: %.4f" % (distancia))
