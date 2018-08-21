# Autor: Erick David Ramírez Martínez, A01748155
# Descripcion: Dados 2 puntos por el usuario, calcular la distancia entre ellos

# Escribe tu programa después de esta línea.

x1=float(input("Introduzca la componente en x del punto A (x1): "))
y1=float(input("Introduzca la componente en y del punto A (y1): "))
x2=float(input("Introduzca la componente en x del punto B (x2): "))
y2=float(input("Introduzca la componente en y del punto B (y2): "))

dist=((x2-x1)**2+(y2-y1)**2)**0.5

print("La distancia entre los dos puntos es de %.4f" % (dist))

