# Autor: Irma Gómez Carmona, A01747743
# Descripcion: Se necesita calcular el porcentaje de hombres y mujeres inscritos, teniendo como referencia el número de hombres y mujeres.

# Escribe tu programa después de esta línea.

mujer= int (input("No. de mujeres inscritas: "))
hombre= int (input("No. de hombres inscritos: "))
totalInscritos =mujer+hombre
promedioH = hombre*100/totalInscritos
promedioM = mujer*100/totalInscritos

print ("Total de inscritos: %d" % (totalInscritos))
print ("Porcentaje de mujeres inscritas: %.1f" %(promedioM),"%")
print ("Porcentaje de hombres inscritos: %.1f" %(promedioH),"%")
