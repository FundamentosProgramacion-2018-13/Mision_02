# Autor: Diana Marisol Medina Bravo, A01748753
# Descripcion: Se calcula el porcentaje de hombres y de mujeres en un grupo con ayuda del número total de personas inscritas, así como, el número de hombres y mujeres

# Escribe tu programa después de esta línea.

numeroM=(int(input("Introduzca el número de mujeres inscritas")))
numeroH=(int(input("Introduzca el número de hombres inscritos")))

numeroTotal=numeroM+numeroH
porcentajeM=(numeroM*100)/numeroTotal
porcentajeH=(numeroH*100)/numeroTotal

print("El porcentaje de hombres es del:%5.2f porciento" %   porcentajeH)
print("El porcentaje de mujeres es del:%5.2f porciento" % porcentajeM)
