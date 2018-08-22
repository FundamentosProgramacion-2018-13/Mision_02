
# Autor: Luis Armando Miranda Alcocer, A01377115
# Descripcion: Al dar dos puntos, calcular distancia entre ambos.

# Escribe tu programa después de esta línea.

x1 = float(input("Ingresa la abscisa del primer punto (eje x): "))
y1 = float(input("Ingresa la ordenada del primer punto (eje y): "))
x2 = float(input("Ingresa la abscisa del segundo punto (eje x): "))
y2 = float(input("Ingresa la ordenada del segundo punto (eje y): "))
d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print ("La distancia entre los dos puntos es: ", '%.4f' % d)
