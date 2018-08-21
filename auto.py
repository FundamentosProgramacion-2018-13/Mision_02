# Autor: Erick David Ramírez Martínez, A01748155
# Descripcion: Con base a la velocidad a la que viaja un auto, calcular la distancia en km que recorre en 4.5 y 7 hrs, así como el tiempo requerido para recorrer 791km

# Escribe tu programa después de esta línea.

vel=float(input("Introduzca la velocidad a la que viaja el vehículo en km/h: "))

dist1=vel*7
dist2=vel*4.5
tiem=791/vel

print("La distancia que recorrerá el vehículo en 7 horas es: %.1f km" %(dist1))
print("La distancia que recorrerá el vehículo en 4.5 horas es: %.1f km" %(dist2))
print("El tiempo necesario para que el vehículo recorra 791km es de: %.1f hrs" %(tiem))

