# Autor: Alberto Contreras Torres, A01748151

# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Escribe un programa que calcula la distancia entre dos puntos.
•	El programa le pregunta al usuario las coordenadas (x1, y1) del primer punto y, también, las coordenadas (x2, y2) del segundo punto.
•	Imprime:
o	La distancia entre los dos puntos.


# Escribe tu programa después de esta línea.
x1= int(input("Teclea X1 :"))
x2= int(input("Teclea X2 :"))
y1= int(input("Teclea Y1 :"))
y2= int(input("Teclea Y2 :"))

d= ((x2-x1)**2+(y2-y1)**2)**.5
print("Distancia= %0.4f"% d)
