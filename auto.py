# Autor: Damián Iván García Ravelo, A01376354
# Descripcion: Calcular el tiempo y distancia, dependiendo del dato dado.

# Escribe tu programa después de esta línea.

# Definir los valores de las variables dadas.
# "t" está dado en horas.
# "d" está dado en kilometros.

t1= 7 #Primer tiempo dado
t2= 4.5 #Segundo tiempo dado
d= 791 #Distancia dada

v=int(input("Introduzca la velocidad del auto en km/h: ")) #El valor que escriba el usuario lo almacenará la variable "v".

#Se despeja la fórmula v=d/t
d1= t1*v #Calcula el valor de la distancia usando el tiempo 1
d2= t2*v #Calcula el valor de la distancia usando el tiempo 2
t= d/v #Calcula el tiempo usando la distancia dada

print("La distancia recorrida en 7 horas es de",format(d1,".1f"), "km")
print("La distancia recorrida en 4.5 horas es de", format(d2,".1f"), "km")
print("El tiempo para recorrer 791km es de", format(t,".1f"), "hr")
