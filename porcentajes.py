# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: Calcular los porcentajes de hombres y mujeres.

# Escribe tu programa después de esta línea

h= int(input("Hombres inscritos: "))
m= int(input("Mujeres inscritas: "))

t= h+m
pM=m*100/t
pH=h*100/t

print("Total de inscritos:  ", t)
print("Porcentaje de mujeres:  %.1f" %(pM),"%")
print("Porcentaje de hombre: %.1f " %(pH),"%")

