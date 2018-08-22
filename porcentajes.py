# Autor:Alexys Martín Coate Reyes, A01746998
# Descripcion: Representar en porcentajes el total de hombres y mujeres inscritos.

"""Elabora un algoritmo y escribe un programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.
# •	El programa le pregunta al usuario el número de mujeres y el número de hombres inscritos.
# •	Imprime:
# o	El número total de alumnos inscritos.
# o	El porcentaje de mujeres.
# o	El porcentaje de hombres."""

# Escribe tu programa después de esta línea.

hombres = int(input("Hombres inscritos: "))
mujeres = int(input("Mujeres inscritas: "))

total = hombres + mujeres
pHombres = (hombres*100)/total
pMujeres = (mujeres*100)/total

print("Total de inscritos: %d" % (total))
print("Porcentaje de hombres: %.1f" % (pHombres), "%")
print("Porcentaje de mujeres: %.1f" % (pMujeres), "%")
