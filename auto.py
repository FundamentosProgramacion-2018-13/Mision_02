# Autor: Saúl Figueroa Conde, A01747306
# Descripcion: Calcula la distancia recorrida por un vehículo con base en la velocidad dada por el usuario.

# Escribe tu programa después de esta línea.




velocidad = input("Indique el valor de la velocidad que desea calcular: ")

resulter1 = int(velocidad)*7
resulter2 = int(velocidad)*4.5
resulter3 = 791/int(velocidad)


print("Velocidad del auto en km/hr: ", velocidad)
print("Distancia recorrida en 7 hrs: ", resulter1, "km.")
print("Distancia recorrida en 4.5 hrs: ", resulter2, "km.")
print("Tiempo para recorrer 791 km: ", resulter3, "hrs.")


