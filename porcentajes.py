# Autor: Erick David Ramírez Martínez, A01748155
# Descripcion: El usuario ingresa un número de mujeres y hombres inscritos en una clase, con base a esto se calcula e imprime el total de alumnos, el porcentaje de hombres y el porcentaje de mujeres en la clase

# Escribe tu programa después de esta línea.

hom=int(input("Introduzca el número de hombres inscritos en la clase: "))
muj=int(input("Introduzca el número de mujeres inscritas en la clase: "))

total=hom+muj
Phom=float(hom)/total*100
Pmuj=float(muj)/total*100

print("Total de alumnos en la clase", total)
print("Porcentaje de hombres: $%.1f" %(Phom))
print("Porcentaje de mujeres: $%.1f" %(Pmuj))

