# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

hombre = int(input("Introduzca la cantidad de hombres en su clase: "))
mujer = int (input("Introduzca la cantidad de mujeres en su clase: "))
print ('Hay', (hombre), 'hombres inscritos')
print ('Hay', (mujer), 'mujeres inscritos')
total = hombre + mujer
print ('El total de alumnos inscritos es de ', (total))
porcentajeMujer = (mujer * 100) / total
porcentajeHombre = (hombre * 100) / total
print ('El porcentaje de mujeres es: %5.1f' % (porcentajeMujer), '%')
print ('El porcentaje de hombres es: %5.1f' % (porcentajeHombre), '%')
