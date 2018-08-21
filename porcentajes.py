# Autor: Diego Armando Ayala Hernández A01376727
# Descripcion: Sacar el porcentaje con regla de 3 a partir de la cantidad de hombre y mujeres que nos dan

# Escribe tu programa después de esta línea.
hombres=input("Cantidad de hombres: ")
mujeres=input("cantidad de mujeres: ")
h=int(hombres)
m=int(mujeres)
total=h+m
phombres=(h*100)/total
pmujeres=(m*100)/total
phombres2=int(phombres)
pmujeres2=int(pmujeres)
print("total de alumnos inscritos: ", total)
print("hombres: ", h)
print("mujeres ",m)
print("porcentaje de hombres: %0.2f"%(phombres),"%")
print("porcentajed de mujeres: %0.2f "%(pmujeres),"%")
