# Autor: Jesus Zabdiel Sanchez Chavez, A01374964
# Descripcion: Programa que calcula la distancia entre dos puntos.

# Escribe tu programa después de esta línea.

x1 = int (input("INserta el valor de x1: "))
y1 = int (input("INserta el valor de x2: "))
x2 = int (input("INserta el valor de y1: "))
y2 = int (input("INserta el valor de y2: "))

distancia = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

print ("La distancia entre los puntos es ", distancia)