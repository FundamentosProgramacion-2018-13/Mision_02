# Autor: luisJonathanRosasRamos, a01377942
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

NMujeres=float(input("Cuantas Mujeres estan Inscritas: "))
NHombres=float(input("Cuantos hombres estan inscritos: "))

Total =NMujeres+NHombres

PMujeres = NMujeres*100/Total
PHombres = NHombres*100/Total

print("El número de alumnos inscritos es de: ", Total)
print("El procentaje de mujeres es de: %5.1f "%(PMujeres), "%")
print("El porcentaje de hombres es de: %5.1f "%(PHombres), "%")
