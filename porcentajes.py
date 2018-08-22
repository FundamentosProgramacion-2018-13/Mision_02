# Autor: Jesús Emmanuel Alcalá Nava , a01376766
# Descripcion: calcular el total de alumnos y el porcentaje de hombres y mujeres de un grupo

# Escribe tu programa después de esta línea.
hombres= int(input("hombres insctritos:"))
mujeres= int(input("mujeres inscritas:"))
total= hombres+mujeres
p1= float((hombres/total)*100)
p2= float((mujeres/total)*100)
print("total de alumnos:", total)
print("porcentaje de hombres: %.1f" % p1, "%") 
print("porcentaje de mujeres: %.1f" % p2, "%") 
