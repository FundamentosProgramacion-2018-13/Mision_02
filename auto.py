# Autor: Carlos Badillo García, A01377618
# Descripcion: Usando la velocidad dada calcular las cifras.

# Escribe tu programa después de esta línea.

vel = int(input("¿A que velocidad viaja el auto? (En km/h): "))
t1 = 7
t2 = 4.5
d1 = 791

dist1preg = vel*t1
dist2preg = vel*t2
tiempo1preg = d1/vel

print("La velocidad que tiene el auto es:", vel)
print("La distancia en km. que recorre en 7hrs. es:", dist1preg)
print("La distancia en km. que recorre en 4.5hrs. es:", dist2preg)
print("El tiempo en horas que requiere para recorrer 791 km. es:", tiempo1preg)
