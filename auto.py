# Autor: Jesús Emmanuel Alcalá Nava, a01376766
# Descripcion: calcular la distancia y el tiempo que recorre un carro en una velocidad dada por el usuario

# Escribe tu programa después de esta línea.
velocidad1= float(input("introduzca la velocidad del auto en términos de km/hr")) 
distancia1= velocidad1*7
distancia2= velocidad1*4.5
tiempo1= 791/velocidad1 
print("distancia recorrida en 7 hrs= %.1f km" % (distancia1))
print("distancia recorrida en 4.5 hrs= %.1f km" % (distancia2))
print("tiempo en el que se recorren 791 km= %.1f hrs" % (tiempo1)) 
