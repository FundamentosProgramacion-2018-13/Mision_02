# Autor: Mariana Caballero Cabrera, A01376544
# Descripcion: A continuación voy a hacer un programa que resuelva la siguiente fórmula (v=d/t) con un dato que el usuario me va a proporcionar y otros que el problema trae incluidos

# Escribe tu programa después de esta línea.

velocidadAuto = float (input("Velocidad a la que va el carro: "))

distanciaSieteHoras = velocidadAuto*7
distanciaCuatroHoras = velocidadAuto*4.5
tiempo = 791/velocidadAuto

print ( "Distancia recorrida en 7 hrs: %5.1f" %(distanciaSieteHoras), "km")
print ( "Distancia recorrida en 4.5 hrs: %5.1f" %(distanciaCuatroHoras), "km")
print ( "Tiempo en recorrer 791 km: %5.4f" %(tiempo), "hrs")
