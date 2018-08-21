# Autor: Humberto Carrillo Gómez, A01377246
#Descripcion: Este programa calcula la distancia que existe entre dos puntos

# Escribe tu programa después de esta línea.

x1= float(input("Teclea x1: "))
y1= float(input("Teclea y1: "))
x2= float(input("Teclea x2: "))
y2= float(input("Teclea y2: "))
distanciaPuntos=((x2-x1)**2+(y2-y1)**2)**(1/2)
print("x1: ",x1)
print("y1: ",y1)
print("x2: ",x2)
print("y2: ",y2)
print("Distancia: ",format(distanciaPuntos,".4f"))   # Resultado con 4 decimales