
# Autor: Luis Armando Miranda Alcocer, a01377115
# Descripcion: Calcula el total, y el porcentaje de mujeres y hombres en una clase.

# Escribe tu programa después de esta línea.

m = int(input("Número de mujeres inscritas: "))
h = int(input("Número de hombres inscritos: "))

total = h + m
print("Número total de alumnos", total)

pM = m/total*100
pH = h/total*100

print("El porcentaje de mujeres es de: ", '%.1f' % pM, "%") 
print("El porcentaje en hombres es de: ", '%.1f' % pH, "%")



