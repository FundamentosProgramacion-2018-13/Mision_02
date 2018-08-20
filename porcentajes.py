# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Calcula el total de alumnos y el porcentaje que hay de cada género

# Escribe tu programa después de esta línea.

hom = int(input("¿Cuántos hombres hay en su salón? "))
muj = int(input("¿Cuántas mujeres hay en su salón? "))

tot = hom + muj
por_hom = (hom/tot) * 100
por_muj = 100 - por_hom

print("Total de alumnos: ", tot)
print("Porcentaje de hombres: %.2f" % por_hom,"%")
print("Porcentaje de mujeres: %.2f" % por_muj,"%")
