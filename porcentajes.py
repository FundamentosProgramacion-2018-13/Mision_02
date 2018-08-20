# Autor: David Rodriguez Fragoso, A01748760
# Descripcion: Problema 4

# Escribe tu programa después de esta línea.

hombres = int(input("Número de hombres: "))
mujeres = int(input("Número de mujeres: "))
total = hombres+mujeres
porcentajeHombres = (hombres/total)*100
porcentajeMujeres = (mujeres/total)*100

print("Hombres inscritos: ", hombres)
print("Mujeres inscritas: ", mujeres)
print("Total inscritos: ", total)
print("Porcentaje de hombres: ", porcentajeHombres, "%")
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
