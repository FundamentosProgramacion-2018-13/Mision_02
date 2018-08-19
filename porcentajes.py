# Autor: Arturo Márquez Olivar, A01376086.
# Descripcion: Saca los porcentajes de hombres y mujeres incritos en una clase, así como el total de ellos.

# Escribe tu programa después de esta línea.

h= input("¿Cuántos hombres hay en la clase?")
m= input("¿Cuántas mujeres hay en la clase?")

t= h+m
ph=h*100/t
pm=m*100/t

print("El total de alumnos inscritos es de: ", t)
print("El porcentaje de hombres es de: ", ph)
print("El porcentaje de mujeres es de: ", pm)
