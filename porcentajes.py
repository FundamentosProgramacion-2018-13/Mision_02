# Autor: Silvia Ferman Muñoz, A01376718
# Descripcion: Calcular el procentaje de Hombres y Mujeres en una clase

# Escribe tu programa después de esta línea.

M = int(input("Cuantas mujeres hay inscritas:"))
H = int(input("Cuantos hombres hay inscritos:"))
talumnos = M + H
pmujeres = (M / talumnos) * 100
phombre = (H / talumnos) * 100

print("El total de alumnos es:", talumnos)
print("El porcentaje de mujeres es: %.1f (%)" % pmujeres)
print("El porcentaje de hombres es: %.1f (%)" % phombres)
