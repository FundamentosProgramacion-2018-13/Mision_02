# Autor: Víctor Manuel Rodríguez Loyola, A01747755
# Descripcion: Este programa calcula el porcentaje de alumnos hombres y mujeres inscritos
#  en una clase, así como el total de alumnos

# Escribe tu programa después de esta línea.

hombres=int(input("Teclea el numero de hombres de la clase "))
mujeres=int(input("Teclea el numero de mujeres de la clase "))

total_alumnos= hombres + mujeres
porc_mujeres= (mujeres*100) / total_alumnos
porc_hombres= (hombres*100) / total_alumnos

print("Mujeres inscritas: ", mujeres)
print("Hombres inscritos: ", hombres)
print("Total de alumnos en la clase: ", total_alumnos)
print("Porcentaje de mujeres: %.1f" % porc_mujeres + "%")
print("Porcentaje de hombres: %.1f" % porc_hombres + "%")
