x1 = int(input("Cual es el valor de x1:"))
x2 = int(input("Cual es el valor de x2:"))
y1 = int(input("Cual es el valor de y1:"))
y2 = int(input("Cual es el valor de y2:"))

dAB = ((x2 – x1)**2 + (y2-y1)**2)**(0.5)
print("La distancia entre A y B es: %.4f" % dAB)
