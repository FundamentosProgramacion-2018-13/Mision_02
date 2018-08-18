# Autor: Jesus Zabdiel Sanchez Chavez, A01374964
# Descripcion: Programa que calcula el porcentaje de mujeres y homnbres inscritos y el total.

# Escribe tu programa después de esta línea.

mujeres = int (input ("Cuantas mujeres estan inscritas: "))
hombres = int (input ("Cuantos hombres estan inscritos "))

total = hombres + mujeres
PorMujeres = (100 * mujeres) / total
PorHombres = (100 * hombres) / total

print ("El numero total de alumnos inscritos es:" , total)
print ("Porcentaje de mujeres: %.2f" % (PorMujeres))
print ("Porcentaje de hombres: %.2f" % (PorHombres))
