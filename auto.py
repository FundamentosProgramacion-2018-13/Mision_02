# Autor:Alexys Martín Coate Reyes, A01746998

# Descripcion: Cacular la distancia y el tiempo con base en la información de la velocidad.

"""La velocidad de un auto puede calcularse con la fórmula v = d/t. (v-velocidad, d-distancia, t-tiempo). Elabora un algoritmo y escribe un programa que pregunte al usuario la velocidad a la que viaja un auto (km/h) y calcule e imprima lo siguiente:
# •	La distancia en km. que recorre en 7 hrs.
# •	La distancia en km. que recorre en 4.5 hrs.
# •	El tiempo en horas que requiere para recorrer 791 km."""

# Escribe tu programa después de esta línea.

v = float(input("Dame la velocidad del auto: "))
t1 = 7
t2 = 4.5
d = 791

R1 = v*t1
R2 = v*t2
R3 = d/v

print("La velocidad del auto es: %.1fkm/h" % (v))
print("Distancia recorrida en %d.1hrs: %.1fkm" % (t1, R1))
print("Distancia recorrida en %d.1hrs: %.1fkm" % (t2, R2))
print("Tiempo en horas que requiere recorrer %.1fkm: %d.1hrs" % (d, R3))

