x_1 = int(input("primer coordenada de x: "))
y_1 = int(input("primer coordenada de y: "))
x_2 = int(input("segunda coordenada de x: "))
y_2 = int(input("segunda coordenada de y: "))

resta_x= x_1-x_2
resta_y=y_1-y_2
cuadradox= resta_x**2
cuadraoy= resta_y**2

distancia= (cuadradox+cuadraoy)**0.5

print("x1: ",x_1)
print("y1: ",y_1)
print("x2: ",x_2)
print("y2: ",y_2)
print("Distancia: ","{0:.4f}".format(distancia))