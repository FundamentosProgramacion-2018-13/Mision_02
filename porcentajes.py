# Autor: Juan Carlos Flores García, A01376511
# Descripcion: Programa que calcula el total de alumnos inscritos y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.
numeroMujeres = int(input("Introduce el número de mujeres: "))
numeroHombres = int(input("Introduce el número de hombres: "))

totalInscritos = numeroMujeres + numeroHombres

porcentajeMujeres = (numeroMujeres*100) / totalInscritos

porcentajeHombres = (numeroHombres*100) / totalInscritos

print("Mujeres Inscritas: ", numeroMujeres)
print("Hombres Inscritos: ", numeroHombres)
print("Total de inscritos: ", totalInscritos)
print("Porcentaje de Mujeres: %.1f %" % porcentajesMujeres)
print("Porcentaje de Hombres: %.1f %" % porcentajeHombres)
