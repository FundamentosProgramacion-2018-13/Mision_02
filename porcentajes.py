# Autor: alejandroToricesOliva, A01377744
# Descripcion: Se calcula el total de alumnos y el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

m = int(input("Ingrese el número de mujeres inscritas en la clase:"))
h = int(input("Ingrese el número de hombres inscritos en la clase:"))

total = m + h
porcentajeMujeres = (m / total) * 100
porcentajeHombres = (h / total) * 100

print("Mujeres inscritas: ", m)
print("Hombres inscritos: ",h)
print("Total de inscritos: ", total)
print("Porcentaje de mujeres: %3.1f" % porcentajeMujeres + "%")
print("Porcentaje de hombres: %3.1f" % porcentajeHombres + "%")
