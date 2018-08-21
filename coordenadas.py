# Autor: Damián Iván García Ravelo, A01376354
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

#Pregunta el valor de x1, x2, y1 y y2
x1=int(input("Ingresa el valor del primer punto en x: "))
y1=int(input("Ingresa el valor del primer punto en y: "))
x2=int(input("Ingresa el valor del segundo punto en x: "))
y2=int(input("Ingresa el valor del segundo punto en y: "))

#Asigna a d como distancia, la cuál se obtiene de la fórmula dada
d= ((x2-x1)**2 + (y2-y1)**2)**0.5

#Imprime el valor de la distancia

print("La distancia e: ", format(d,".4f"))