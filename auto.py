# Autor: Luis Armando Miranda Alcocer, A01377115
# Descripcion: Al dar la velocidad, calcula la distancia en 7 y 4.5 horas, y el tiempo para recorrer 791 km.

# Escribe tu programa después de esta línea.

v = float(input("Velocidad del auto en km/h: "))
d7 = v*7
d45 = v*4.5
t=791/v
print (" La distancia recorrida en 7 horas es: ", d7, " km")
print (" La distancia recorrida en 4.5 horas es: ", d45, " km")
print (" El tiempo para recorrer 791 km es: ", '%.4f'% t, " horas") #%.4f es para 4 decimales.

