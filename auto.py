# Autor: Luis Ricardo Chagala Cervantes, A01376951
# Descripcion: 
#1.	Leer la velocidad del auto.
#2.	Calcular la distancia recorrida en 7 horas multiplicando la velocidad por 7.
#3.	Calcular la distancia recorrida en 4 horas y media multiplicando la velocidad por 4.5.
#4.	Calcula el tiempo dividiendo 791 km entre la velocidad.
#5.	Imprime Distancia recorrida en 7 hrs.
#6.	Imprime Distancia recorrida en 4.5 hrs.
#7.	Imprime el tiempo después de 791 km.


# Escribe tu programa después de esta línea.
v = int(input("Velocidad del auto en km/h: "))

distanciaen7hrs = v * 7
distanciaen4hrsymedia = v * 4.5
tiempo = 791 / v

print ("Distancia recorrida en 7hrs = " , distanciaen7hrs)
print ("Distancia recorrida en 4.5hrs = " , distanciaen4hrsymedia)
print ("Tiempo para recorrer 791km/h = " , tiempo)
