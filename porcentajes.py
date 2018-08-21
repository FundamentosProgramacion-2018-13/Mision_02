# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
hombres=int(input("Hombres",))
mujeres=int(input("Mujeres",))
total=hombres+mujeres
porcentajeHombres=(hombres*100)/total
porcentajeMujeres=(mujeres*100)/total
print "Hombres inscritos:",hombres
print"Mujeres inscritas:",mujeres
print"Total de inscritos:",total
print"Porcentaje de hombres:",porcentajeHombres,"%"
print"Porcentaje de mujeres:",porcentajeMujeres,"%"