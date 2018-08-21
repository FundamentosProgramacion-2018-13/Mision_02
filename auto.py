# Autor: Jose Luis Mata Lomelí, A01377205
# Descripcion: Sacar la distancia y el tiempo de una velocidad definida por el usuario
# Escribe tu programa después de esta línea.

velocidad= int(input("Escriba la velocidad del vehiculo: "))

tiempo_1= int("7")
tiempo_2= float("4.5")
distancia= float("791")

distancia_formula_a= velocidad*tiempo_1
distancia_formula_b= velocidad*tiempo_2

tiempo_formula= distancia/velocidad


print("Velocidad del vehiculo: ", (velocidad))
print("Distancia recorrida en", (tiempo_formula)," horas es:", (distancia_formula_a))
print("Distancia recorrida en", (tiempo_2), " horas es:" , (distancia_formula_b))
print("Tiempo para recorrer ", (distancia) ,"seria: ", (tiempo_formula))

