# Autor: Mariana Caballero, A01376544
# Descripcion: A continuación voy a crear un programa que calcule el número de personas que hay en un grupo, así como el porcentaje de mujeres y hombres dentro de ese grupo

# Escribe tu programa después de esta línea.

mujeres =  int (input("Mujeres inscritas: "))
hombres = int (input("Hombres inscritos?: "))

totalPersonas = mujeres+hombres
porcentajeMujeres = mujeres*100/totalPersonas
porcentajeHombres = hombres*100/totalPersonas

print ("Total de inscritos:" , totalPersonas)
print ("Porcentaje de mujeres: %5.1f"  %(porcentajeMujeres) ,"%")
print ("Porcentaje de hombres: %5.1f"  %(porcentajeHombres) ,"%")
