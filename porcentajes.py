# Autor: Javier Alexandro Vargas Sánchez, A01377718
# Descripcion: Este programa calcula el número total de alumnos, y los porcentajes totales divididos por sexo .

# Escribe tu programa después de esta línea.
alumMujeres = (int(input("Teclea el número de alumnas inscritas en la escuela:     ")))

alumHombres = (int(input("Teclea el número de alumnos inscritos en la escuela:     ")))

totalDeAlumnos =  alumHombres + alumMujeres

porcenMuj = (alumMujeres * 100) / totalDeAlumnos

porcenHom = (alumHombres* 100) / totalDeAlumnos

print ("Total de alumnas:  ", alumMujeres)

print ("Total de alumnos:  ", alumHombres)

print("El total de alumnos es de:  ", totalDeAlumnos)

print ("Este es el porcentaje de alumnas:   ", porcenMuj)

print ("Mientras que, este es el porcentaje de alumnos:   ", porcenHom)
