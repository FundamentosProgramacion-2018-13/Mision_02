# Autor: Humberto Carrillo Gómez, A01377246
'''Descripcion: Este programa calcula la distancia que será recorrida en 7 y 4.5 hrs, además, calcula el tiempo para
                recorrer 791 km'''

# Escribe tu programa después de esta línea.

velocidad=int(input("Teclea tu velocidad: "))
distancia7= velocidad*7
distancia4_5= velocidad*4.5
tiempo791= 791/velocidad

print("Tu velocidad es:", velocidad,"km/h")
print("La distancia recorrida en 7 horas es:",format(distancia7,".1f"),"km/h")       # Resultados con un solo decimal
print("La distancia recorrida en 4.5 horas es:",format(distancia4_5,".1f"),"km/h")
print("El tiempo necesario para recorrer 791 km es:",format(tiempo791,".1f"), "hrs")
