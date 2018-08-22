# Autor: Javier Alexandro Vargas Sánchez, A01377718
"""Descripcion: Con este programa se puede calcular la distancia entre dos puntos"""

# Escribe tu programa después de esta línea.

#Coordenada inicial
px1=(int(input("Teclea el punto de inicio del recorrido en el eje x:    ")))
py1=(int(input("Teclea el punto de inicio del recorrido en el eje y:    ")))
#Coordenada final
px2=(int(input("Teclea el punto final del recorrido en el eje x:    ")))
py2=(int(input("Teclea el punto final del recorrido en el eje y:    ")))



distanciaEntrePuntos= (((px2 - px1)**2 + (py2 - py1)**2)**.5)

print("La distancia total entre el punto de inicio y fin del recorrido es de:   ", format(distanciaEntrePuntos, ".3f" ))

