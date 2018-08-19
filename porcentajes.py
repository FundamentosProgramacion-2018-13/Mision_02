# Autor: Sebastian Macias Ibarra, A01376492
# Descripcion: Calcular total de inscritos, porcentaje de mujeres y porcentaje de hombres.

# Escribe tu programa después de esta línea.
mujeres = int ( input("Escribe el número de mujeres inscritas: "))
hombres = int ( input("Escribe el número de hombres inscritos: "))

total = mujeres + hombres
porcentajeMujeres = (mujeres * 100) / total
porcentajeHombres = (hombres * 100) / total

print("Total de alumnos inscritos: ", total)
print("Porcentaje de mujeres inscritos: %.1f" % porcentajeMujeres, "%")
print("Porcentaje de hombres inscritos: %.1f" % porcentajeHombres, "%")
