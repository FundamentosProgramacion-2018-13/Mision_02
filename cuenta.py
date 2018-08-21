# Autor: Damián Iván García Ravelo, A01376354
# Descripcion: Sumar la propina y el iva al costo de la comida.

# Escribe tu programa después de esta línea.

cc= int(input("¿Cuál es el total de la comida? $"))  #Pregunta y almacena el valor dado del costo de la comida
p= cc*0.13  #Calcula el valor de la propina
iva= cc*0.15 #Calcula el valor del iva
ct= cc+p+iva  #Suma el costo de la comida con la propina y el iva

print ("La propina es de $", format(p,".2f"))
print("El IVA es de $", format(iva,".2f"))
print("El costo total es de $",format(ct,".2f"))
