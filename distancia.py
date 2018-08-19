#Autor: Arturo Márquez Olivar, A01376086
#Desripción: Imprime la distancia entre 2 puntos.

#Escribe tu programa después de esta línea.

x1= input("¿Cuál es el valor de x1?")
y1= input("¿Cuál es el valor de y1?")
x2= input("¿Cuál es el valor de x2?")
y2= input("¿Cuál es el valor de y2?")

d=( ((x2-x1)**2) + ((y2-y1)**2) )**0.5

print("Distancia= ", d)
