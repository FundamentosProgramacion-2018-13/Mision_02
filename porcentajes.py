# Autor: María Fenanda Vela Calderón, A01377958
# Descripcion: Calcular el total de alumnos y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.

m = int( input( "Escribe el número de mujeres inscritas: "))
h = int( input( "Escribe el número de hombres inscritos: "))

total = m+h

pm = m*100/total     #Porcentje mujeres

ph = h*100/total     #Porcentje hombres
 
print( "Mujeres inscritas: ", m)
print( "Hombres inscritos: ", h)
print( "Total de alumnos inscritos: ", total)
print( "Porcentaje de mujeres: %9.01f " % pm, "%")
print( "Porcentaje de hombres: %9.01f " % ph, "%")
