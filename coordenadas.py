# Autor: Luis Rcardo Chagala Cervantes, A01376951
# Descripcion: 
#1.	Leer x1.
#2.	Leer y1.
#3.	Leer x2.
#4.	Leer y2.
#5.	Sumar (x2-x1)2 más (y2-y1)2 donde todo el conjunto este elevado a 0.5.
#6.	Imprimir distancia.

# Escribe tu programa después de esta línea.
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia = ((x2-x1)**2+(y2-y1)**2)**.5

print ("Distancia = " , distancia)
