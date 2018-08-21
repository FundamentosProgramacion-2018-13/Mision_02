# Autor: Ivan Honc Ayón, A01376466
# Descripcion: Este programa calcula porcentajes de mujeres y hombres en un grupo.

# Escribe tu programa después de esta línea.

numerom = float(input("Dame el número de mujeres inscritas: "))
numeroh = float(input("Dame el número de hombres inscritos: "))

total = numerom + numeroh
porcentajesm = (numerom/total)*100
porcentajesh = (numeroh/total)*100
print("""
Total de alumnos inscritos: %d
Porcentaje de mujeres inscritas: %5.2f%%
Porcentaje de hombres inscritos: %5.2f%%""" % (total, porcentajesm, porcentajesh))
