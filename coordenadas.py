#Autor: Alex Serrano Durán, A01376364
#Descripcion: Este programa calcula la distancia entre dos coordenadas

x1 = int(input("x1= "))
y1 = int(input("y1= "))
x2 = int(input("x2= "))
y2 = int(input("y2= "))

d1 = (((x2-x1)**2)+((y2-y1)**2))
d = d1**.5
print("Distancia: %.4f" % d)
