# Autor: Joshua Sánchez Martínez, A01274269
# Descripcion: Dar a conocer el total de alumnos y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.

hombres = int(input("Teclea el numero de hombres inscritos: "))
mujeres = int(input("Teclea el numero de mujeres inscritas: "))

total = hombres+mujeres
pmujeres = mujeres/total*100
phombres = hombres/total*100

print("total de alumnos inscritos: ", total)
print("Porcentaje de mujeres inscritas: %.1f" % pmujeres, "%")
print("Porcentaje de hombres inscritos: %.1f" % phombres, "%")