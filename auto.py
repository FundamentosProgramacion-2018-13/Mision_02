# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripcion: Pide que calcular la distancia del auto en 7 horas, en 4.5hrs, la distancia en 791km y todo esto en base a la velocidad introducida por el usuario.

# Escribe tu programa después de esta línea.
v=int(input("Escriba la velocidad de su auto (km/h): "))
d7 = v * 7
d4_5 = v * 4.5
t791 = 791 / v

print("La velocidad de su auto es: ", v,"km")
print("La distancia que recorre en 7 hrs es: %0.1f" % (d7), " km")
print("La distancia que recorre en 4.5 hrs es: %0.1f" % (d4_5), " km")
print("El tiempo para recorrer 791km es: %0.4f" % (t791), " hrs ")
