# Autor: alejandroToricesOliva, A01377744
# Descripcion: Cálculo de la distancia dados dos puntos en un plano cartesiano.

# Escribe tu programa después de esta línea.

x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de y2: "))

d = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

print("x1: ", x1)
print("y1: ", y1)
print("x2: ", x2)
print("y2: ", y2)
print("Distancia: %5.4f" % d)
