# Autor: Daniel Córdova Bermúdez, A01377242
# Descripcion:El programa calcula la canitdad de alumnos inscritos junto con el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.

mujeres_i = float(input("Número de mujeres incritas:"))
hombres_i = float(input("Número de hombres inscritos;"))


total = mujeres_i + hombres_i
mujeres_p = mujeres_i/total*100
hombres_p = hombres_i/total*100


print("""
Total de inscritos:  %d
Porcentaje de mujeres: %.1f
Porcentaje de hombres: %.1f
""" %(total,mujeres_p,hombres_p))
