# Autor: Luis Mario Cervantes Ortiz , A01376958
# Descripcion: Saber el numero total de alumnos en una escuela y saber los porcentajes de hombres y mujeres inscritas

# Escribe tu programa después de esta línea.
muj=input("Numero de mujeres: ")
hom=input("Numero de hombres: ")
muj=int(muj)
hom=int(hom)
total= (muj+hom)
print("Total de alumnos: ",total)
total=int(total)

Porcentajemuj=(((muj*100))/total)
print("Porcentaje de Mujeres: %.1f" %Porcentajemuj)
Porcentajehom=((hom*100)/total)
print("Porcentaje de Hombres: %.1f" % Porcentajehom)