# Autor: Zoe Caballero Dominguez, A01747247
# Descripcion: Dado el número de alumnas y alumnos inscritos, calcula el total de alumnos y el porcentaje correspondiente a la cantidad de mujes y a la cantidad de hombres

# Escribe tu programa después de esta línea.
numeroMujeres = int(input("Mujeres inscritas:"))
numeroHombres = int(input("Hombres inscritos:"))

totalAlumnos = numeroHombres + numeroMujeres
porcentajeMujeres = (numeroMujeres * 100)/totalAlumnos
porcentajeHombres = (numeroHombres * 100)/ totalAlumnos

print ("Total de inscritos:", totalAlumnos)
print ("Porcentaje de Mujeres: %.1f" % (porcentajeMujeres), "%")
print ("Porcentaje de Hombres: %.1f" % (porcentajeHombres), "%")
