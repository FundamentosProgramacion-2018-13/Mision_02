# Autor: Mariana Caballero, A01376544 
# Descripcion: A continuación voy a crear un programa que calcule el número de personas que hay en un grupo, así como el porcentaje de mujeres y hombres dentro de ese grupo

# Escribe tu programa después de esta línea.

mujeres = input int("Cuántas mujeres hay?: ")
hombres = input int("Cuántos hombres hay?: ")

totalPersonas = mujeres+hombres
porcentajeMujeres = mujeres*100/totalPersonas
porcentajeHombres = hombres*100/totalPersonas

print ("Total de inscritos:" , totalPersonas)
print ("Porcentaje de mujeres inscritas: %5.2f"  %(porcentajeMujeres  "%")
print ("Porcentaje de hombres inscritos: %5.2f"  %(porcentajeHombres  "%")
