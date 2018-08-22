# Autor: Carlos Badillo García, A01377618
# Descripcion: Usando el total de hombres y mujeres, calcular el número total de alumnos, y los porcentajes tanto de hombres como de mujeres.

# Escribe tu programa después de esta línea.

th = int(input("¿Cuántos hombres están inscritos?"))
tm = int(input("¿Cuántas mujeres están inscritas?"))
ta = th+tm
porcenth = (th/ta)*100
porcentm = (tm/ta)*100

print("El total de alumnos inscritos es de:", ta)
print("El porcentaje de hombres en la clase es de: %", porcenth)
print("El porcentaje de mujeres en la clase es de: %", porcentm)
