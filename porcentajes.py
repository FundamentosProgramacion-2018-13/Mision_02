# Autor: Jesús Roberto Herrera Vieyra, A01377230
# Descripcion: Programa que calcula el total de alumos y los porcentajes de cada género
# Escribe tu programa después de esta línea.
mujeres = int(input("Número de mujeres: "))
hombres = int(input("Número de hombres:"))

total= hombres+mujeres
porcentajeH= (hombres*100)/total
porcentajeM=(mujeres*100)/total

print("Total de alumnos: ",(total))
print("Porcentaje de mujeres: ","{0:.1f}".format(porcentajeM),"%")
print("Porcentaje de hombres: ","{0:.1f}".format(porcentajeH),"%")
