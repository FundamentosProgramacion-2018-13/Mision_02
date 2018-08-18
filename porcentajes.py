# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripcion: Calcular el porcentaje de hombres y mujeres con base a las mujeres que hay en total y hombres en total.

# Escribe tu programa después de esta línea.

h=int(input("¿Cuantos hombres hay en total? "))
m=int(input("¿Cuantas mujeres hay en total? "))
total= h+m
pm= m*100/total
ph= h*100/total

print("Mujeres inscritas: ",m)
print("Hombres inscritos: ",h)
print("Total de estudiantes: ",total)
print("Porcentaje de mujeres: ",pm)
print("Porcentaje de hombres: ",ph)
