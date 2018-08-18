# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripcion: Calcular la distancia entre dos puntos con solo las coordenadas.

# Escribe tu programa después de esta línea.

px1=float(input("Escribe la coordenada x del primer punto: "))
py1=float(input("Escribe la coordenada y del primer punto: "))
px2=float(input("Escribe la coordenada x del segundo punto: "))
py2=float(input("Escribe la coordenada y del segundo punto: "))

d= (((px2-px1)**2)+((py2-py1)**2))**0.5

print("x1: ",px1)
print("y1: ",py1)
print("x2: ",px2)
print("y2: ",py2)
print("Distancia: %0.4f" %(d))
