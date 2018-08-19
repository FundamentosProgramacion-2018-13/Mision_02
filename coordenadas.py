# Autor: Víctor Manuel Rodríguez Loyola, A01747755
# Descripcion: Este programa calcula la distancia entre dos puntos
# en el plano cartesiano, a partir de los valores de X y Y que ingrese el usuario

# Escribe tu programa después de esta línea.

x1=int(input("Teclea el valor de x1 "))
y1=int(input("Teclea el valor de y1 "))
x2=int(input("Teclea el valor de x2 "))
y2=int(input("Teclea el valor de y2 "))

distancia=((x2-x1)**2 + (y2-y1)**2)**0.5

print("x1= ",x1)
print("y1= ",x2)
print("x2= ",x2)
print("y2= ",y2)
print("La distancia entre los dos puntos es: %.4f" % distancia)

