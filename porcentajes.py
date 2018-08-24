# Autor: Jonathan Sanabria Rocha, A01746763
# Descripcion: Porcentajes de hombre y mujeres inscritos presentando los porcentajes con un solo decimal.

# Escribe tu programa después de esta línea.
hombres=float(input("Dame el numero de Hombre inscritos: "))
mujeres=float(input("Dame el numero de mujeres inscritas: "))
totinscritos=hombres+mujeres
porch=hombres/totinscritos*100
porcm=mujeres/totinscritos*100
print("Hombres inscritos: %s" %(hombres))
print("Mujeres inscritas: %s" %(mujeres))
print("Total de inscritos: %s" %(totinscritos))
print("Porcentaje de hombres: ",format(porch,".1f"))
print("Porcentaje de mujeres: ",format(porcm,".1f"))
