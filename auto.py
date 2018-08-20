# Autor: Zabdiel Valentin Garduño Vivanco, A01377950.
# Descripcion: A traves de una velocidad dada en Km/Hora sacer la distancia en 7 y 4.5horas, además del tiempo en 791 m.

# Escribe tu programa después de esta línea

v= int(input("Teclea la velocidad del auto(Km/Hora-enteros): "))

d1=v*7
d2=v*4.5
t=791/v


print("Distancia recorrida en 7 hrs:  ", d1)
print("Distancia recorrida en 4.5 hrs:  ", d2)
print("Tiempo para recorrer 791 km: %10.4f" % (t))



