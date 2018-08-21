
# Autor: Humberto Carrillo Gómez, A01377246
# Descripcion: Este proglama calcula el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

m=int(input("Teclea el número de mujeres inscritas: "))
h=int(input("Teclea el número de hombres inscritos: "))
numeroTotal= m+h
porcentajemujeres= (m*100)/numeroTotal
porcentajehombres= (h*100)/numeroTotal
print("Mujeres inscritas: ", m)
print("Hombres inscritos: ", h)
print("Total de inscritos: ", numeroTotal)
print("Porcentaje de mujeres: ",format(porcentajemujeres,".1f"),"%")
print("Porcentaje de hombres: ",format(porcentajehombres,".1f"),"%")
