mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

alumnos = mujeres + hombres
porcentajem = mujeres * 100 / alumnos
procentajeh = hombres * 100 / alumnos

print("Total de alumnos inscritos:", alumnos)
print("Porcentaje de mujeres: %.1f" % (porcentajem) + "%")
print("Porcentaje de hombres: %.1f" % (procentajeh) + "%")