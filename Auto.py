# Autor:Oscar Macias Rodríguez, A01376398
# Calcule la distancia y el tiempo usando la fórmula de velocidad


v = int (input("Velocidad del auto en kn/h:"))
d1 = v*7
d2 = v*4.5
t = 791/v

print("Distancia recorrida en 7 hrs: ", "%.1f" % d1, " km")
print("Distancia recorrida en 4 hrs:", "%.1f" % d2, "km")
print("Tiempo para recorrer 791 km:", "%.1f" % t, "hrs.")