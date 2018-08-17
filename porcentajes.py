# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula porcentaje de alumnos de ambos sexos

"""
Analisis:
E: H, M
S: total, %H, %M
E/S:
total = H+M
%H=H/total
%M=M/total

Algoritmo:
Preguntar numero de hombres y mujeres y asignar cada uno a una variable
Sumar variables y reportar total
Dividir numero de hombres entre total y reportar
Restar porcentaje de hombres a 100 y reportar
"""

H = int(input("Numero de Hombres: "))
M = int(input("Numero de Mujeres: "))
total = H+M
print("El total de alumnos es: " + str(total))
Hpor = H/total*100
print("El porcentaje de hombres es: " + "{:,.1f}%".format(Hpor))
print("El porcentaje de mujeres es: " + "{:,.1f}%".format(100-Hpor))
