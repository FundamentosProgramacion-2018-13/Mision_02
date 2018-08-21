# Autor: Jesús Roberto Herrera Vieyra, A01377230
# Descripcion: Programa para calcular la distancia de 7 y 4.5 hrs y y el tiempo en el que se recorren 791 km

# Escribe tu programa después de esta línea.
velocidad = float(input("Velocidad del coche en Km/Hr: "))

distancia1 = velocidad*7
distancia2= velocidad*4.5
tiempo= 791/velocidad

print("En 7 horas se recorrieron ", (distancia1), " km")
print("En 4.5 horas se recorrieron ", (distancia2), " km")
print("Se recorrieron 791 km ", "{0:.1f}".format(tiempo), " horas")
