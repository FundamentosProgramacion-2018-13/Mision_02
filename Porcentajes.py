# Autor:Oscar Macias Rodríguez, A01376398
# Calcula el porcentaje de hombres y mujeres inscritos en una clase


m = int(input("Mujeres inscritas:"))
h = int(input("Hombres inscritos:"))
total = m+h
p1 = m*100/total
p2 = h*100/total

print("Total de inscritos:", total)
print("Porcentaje de mujeres:", "%.1f" % p1)
print("Porcentaje de hombres:", "%.1f" % p2)