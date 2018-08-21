# Autor: Alex Fernando Leyva Martínez, A01747078
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Obtner el porcentaje de hombres y mujeres con respecto al total de alumnos tomando en cuenta la cantidad de hombres y mujeres dadas.
# Escribe tu programa después de esta línea.
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

total = (hombres + mujeres)
porM = float(mujeres * 100 / total)
porH = float(hombres * 100 / total)

print("Total de inscritos: ",total)
print("Porcentaje de mujeres: %.1f"% porM, "%")
print("Porcentaje de hombres: %.1f"% porH, "%")
