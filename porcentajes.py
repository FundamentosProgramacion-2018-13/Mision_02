# Autor: Irma Gómez Carmona, A01747743
# Descripcion: Se necesita calcular el porcentaje de hombres y mujeres inscritos, teniendo como referencia el número de hombres y mujeres, 
#los cuales son introducidos por el usuario.

# Escribe tu programa después de esta línea.

Nmujeres= int (input("No. de mujeres inscritas: "))
Nhombres= int (input("No. de hombres inscritos: "))
totalInscritos =Nmujeres+Nhombres
promedioH = Nhombres*100/totalInscritos
promedioM = Nmujeres*100/totalInscritos

print ("Total de inscritos: %d" % (totalInscritos))
print ("Porcentaje de mujeres inscritas: %.1f" %(promedioM),"%")
print ("Porcentaje de hombres inscritos: %.1f" %(promedioH),"%")
