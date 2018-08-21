# Autor: Carlos Alberto Reyes Ortiz, A01376349
# Descripcion: Te ayuda a calcular el porcentaje de mujeres y hombres que hay inscritos en una clase, como el total de alumnos inscritos

# Escribe tu programa después de esta línea.
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

totalInscritos = mujeres + hombres
porcentajeMujeres = mujeres*100/totalInscritos
porcentajeHombres = hombres*100/totalInscritos

print("Total de inscritos:",totalInscritos)
print("Porcentaje de mujeres:", "{:.1f}" . format(porcentajeMujeres),"%")
print("Porcentaje de hombres", "{:.1f}" . format(porcentajeHombres),"%")
