# Autor: Roberto Emmanuel González Muñoz A01376803
# Este programa calcula la velocidad, distancia y
# tiempo de un problema dado.

#El usuario introduce la velocidad
velocidad = int(input("Introdusca la velocidad del auto: "))

#variables globales
distanciaN7H = velocidad*7
distanciaN4d5H = velocidad*4.5
tiempo791 = 791/velocidad

print("Velocidad del auto es: ",format(velocidad,".1f"),"km/hr")
print("La distancia recorrida en 7 horas es: ",format(distanciaN7H,".1f"),"km")
print("La distancia recorrida en 4.5 horas es: ",format(distanciaN4d5H,".1f"),"km")
print("Tiempo para recorrer 791 km: ",format(tiempo791,".1f"),"hrs")
