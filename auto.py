# Autor: alejandroToricesOliva, A01377744
# Descripcion: Recorrido y tiempo de un auto conociendo su velocidad

# Escribe tu programa después de esta línea.
v = float(input("Introduzca la velocidad en km/h:"))

d1 = v * 7
d2 = v * 4.5
t = 791/v

print("Velocidad del auto es de:", v, "km/h")
print("La distancia a las 7hrs es: ", d1,"km")
print("La distancia a las 4.5hrs es: ", d2,"km")
print("El tiempo que tarda en recorrer 791km es: %6.2f" % t, "hrs")
