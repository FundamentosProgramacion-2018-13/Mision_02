mujeres = int(input("Introduzca el número de mujeres: "))
hombres = int(input("Introduzca el número de hombres: "))
total = mujeres + hombres
pormujeres = mujeres / total * 100
porhombres = hombres / total * 100
print("Total de inscritos: ", total)
print("Porcentaje de mujeres: {:.1f}%" .format(pormujeres))
print("Porcentaje de hombres: {:.1f}%" .format(porhombres))