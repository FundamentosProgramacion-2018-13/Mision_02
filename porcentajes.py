# Autor: Damián Iván García Ravelo, A01376354
# Descripcion: Calcular el porcentaje de hombres y mujeres que hay.

# Escribe tu programa después de esta línea.

h = int(input("Ingresa el número total de hombres: ")) #Pregunta el total de hombres
m = int(input("Ingresa el número total de mujeres: ")) #Pregunta el total de mujeres
t = h+m #Suma el número de hombres y mujeres
porcentajeHombres = (h/t) * 100
porcentajeMujeres = (m/t) * 100

print ("El número total de alumnos inscritos es: ",t)
print ("El porcentaje de mujeres isncritas es: %", format(porcentajeMujeres, ".1f"))
print ("El porcentaje de hombres inscritos es: %", format(porcentajeHombres, ".1f"))
