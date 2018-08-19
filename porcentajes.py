#Autor: Alex Serrano Durán, A01376364
#Descripcion: Este programa calcula el total de alumnos en un curso y el porcentaje por sexo

m = int(input("Cantidad de mujeres inscritas: "))
h = int(input("Cantidad de hombres inscritos: "))

t = m+h
mPorcentaje = float((m/t)*100)
hPorcentaje = float((h/t)*100)

print("Total de alumnos: ", t)
print("Porcentaje de mujeres: %.1f" % mPorcentaje, "%")
print("Porcentaje de hombres: %.1f" % hPorcentaje, "%")
