# Autor: Arturo Márquez Olivar, A01376086
# Descripcion: Genera la cuenta total del costo de una comida dada por el problema 3.

# Escribe tu programa después de esta línea.

c= input("¿Cuál fue el costo de tu comida?")

p= c*(0.13)
i= c*(0.15)
ct= c+p+i

print("El costo de tu comida fue: ", c)
print("La propina debería de ser de: ", p)
print("El iva debería ser de: ", i)
print("El costo total de tu comida es de: ", ct)
