# Autor: Saúl Figueroa Conde, A01747306
# Descripcion: Programa que calcula el porcentaje de hombres y mujeres (alumnos) inscritos.

# Escribe tu programa después de esta línea.


mujerese = int(input("Escriba el número de mujeres inscritas: "))
hombrese = int(input("Escriba el número de hombres inscritos: "))

total = hombrese + mujerese
pormuj = ((mujerese) * (100)) / total
porhom = ((hombrese) * (100)) / total

print("El total de alumnos es: ", total)
print("El porcentaje de mujeres es: ", "%.1f"% pormuj,"%")
print("El porcentaje de hombres es: ", "%.1f"% porhom, "%")