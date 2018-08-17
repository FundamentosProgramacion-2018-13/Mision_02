# Autor: Samantha Martínez Franco, A01747686
# Descripcion: Calcular el porcetaje de hombres en el grupo

# Escribe tu programa después de esta línea.

hombres=int(input("Hombre inscritos:"))
mujeres=int(input("Mujeres inscritas:"))
totalAlumnos=hombres+mujeres
porcentajeH=hombres*100/totalAlumnos
porcentajeM=mujeres*100/totalAlumnos

print("Total inscritos:",totalAlumnos)
print("Porcentaje de mujeres: %5.1f" % (porcentajeM),"%")
print("Porcentaje de hombres: %5.1f" % (porcentajeH),"%")
