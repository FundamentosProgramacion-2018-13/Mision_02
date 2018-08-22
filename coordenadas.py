# Autor: Rubén Villalpando Bremont, A01376331, grupo 4
# Descripcion: Programa que le pregunta al usuario las coordenadas de 2 puntos y el programa le devuelve la distancia entre ellos.

# Escribe tu programa después de esta línea
x1 = int(input("Escriba las coordenadas del punto X1: "))
y1 = int(input("Escriba las coordenadas del punto Y1: "))
x2 = int(input("Escriba las coordenadas del punto X2: "))
y2 = int(input("Escriba las coordenadas del punto Y2: "))
distanciaEntrePuntos = (((x2-x1)**2)+((y2-y1)**2))**0.5
print("Distancia entre los puntos: ", distanciaEntrePuntos)

