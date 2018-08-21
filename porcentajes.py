# Autor: Alek Fernando Howland Aguilar, A01747765
# Descripcion: Un programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.


print ("Bienvenido")
print ("..............")

mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))
total = mujeres + hombres
por_muj = (mujeres * 100) / total
por_hom = (hombres * 100) / total 

print ("..............")

print ("Total de inscritos:", total)
print ("Total de mujeres:", mujeres)
print ("Total de hombres:", hombres)

print ("..............")

print ("Porcentaje de mujeres: %.1f " % (por_muj), ("%"))
print ("Porcentaje de hombres: %.1f" %  (por_hom), ("%"))

print ("..............")
print ("Gracias")
