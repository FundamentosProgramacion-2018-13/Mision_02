# Autor: Rubén Villalpando Bremont, A01376331, grupo 4
# Descripcion: El programa le pide al usuario que ingrese el número de hombres y mujeres que hay inscritos y le devuelve el número total
#de alumnos inscritos y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.
numeroMujeres = int(input("Ingrese el número de mujeres inscritas: "))
numeroHombres = int(input("Ingrese el número de hombres inscritos: "))
totalInscritos = numeroHombres + numeroMujeres
porcentajeHombres = (numeroHombres/totalInscritos)*100
porcentajeMujeres = (numeroMujeres/totalInscritos)*100
print("Mujeres inscritas: ", numeroMujeres)
print("Hombres inscritos: ", numeroHombres)
print("Total de inscritos: ", totalInscritos)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
print("porcentaje de hombres: ", porcentajeHombres, "%")
