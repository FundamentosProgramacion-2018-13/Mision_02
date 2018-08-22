# Autor: Roberto Emmanuel González Muñoz A01376803
# Este programa calcula la distancia entre dos puntos.

#El usuario introduce las coordenadas del punto 1 y 2
puntoAX = int(input("Introduce la coordenada X del Punto A: "))
puntoAY = int(input("Introduce la coordenada Y del Punto A: "))
puntoBX = int(input("Introduce la coordenada X del Punto B: "))
puntoBY = int(input("Introduce la coordenada Y del Punto B: "))

restaX = (puntoBX-puntoAX)**2
restaY = (puntoBY-puntoAY)**2
distancia = (restaX+restaY)**(1/2)

print("X1: ",puntoAX)
print("Y2: ",puntoAY)
print("X2: ",puntoBX)
print("Y2: ",puntoBY)
print("La distancia entre A y B es: ",format(distancia,".4f"))