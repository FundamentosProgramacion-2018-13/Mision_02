# Autor: Alek Fernando Howland Aguilar
# Descripcion: Un programa que pregunte al usuario la velocidad a la que viaja un auto (km/h) y calcule diferentes incisos.
# Escribe tu programa después de esta línea.

print ("Bienvenido")
print ("."*20)

velocidad_usuario = float(input("Cual es la velocidad del auto:"))
print ("."*20)

A = velocidad_usuario*7
B = velocidad_usuario*4.5
C = 791/velocidad_usuario

print ("Distancia recorrida en 7 hrs: %.1f " % (A) ,("km"))
print ("Distancia recorrida en 4 hrs: %.1f " % (B), ("km"))
print ("Tiempo en que se recorren los 791 km: %.1f " % (C))

print ("."*20)

`
