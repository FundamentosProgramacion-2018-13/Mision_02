# Autor: Daniel Córdova Bermúdez, A01377242
# Descripcion: El programa calcula la distancia en que recorre un auto a 7 horas y 4.5 además del tiempo para recorrer 791.

# Escribe tu programa después de esta línea.

velocidad = float(input("Velocidad en k/m:"))
distancia_1 = velocidad * 7
distancia_2 = velocidad * 4.5
tiempo = 791 / velocidad
print("Distancia recorrida en 7 horas:%.1f" %(distancia_1))
print("Distancia recorrida en 4.5 horas:%.1f" %(distancia_2))
print("Tiempo en recorrer en 791 km/h:%.1f" %(tiempo))
