# Autor: Carlos Alberto Reyes Ortiz
# Descripcion: Calcula la distancia en km, en un tiempo de 7 hrs, 4.5hrs y la velocidad dada por el usuario. También puede calcular
# El tiempo que tarda en hrs, en una distancia de 791km, igual por la velocidad dada por el usuario.
# Escribe tu programa después de esta línea.
tiempoUno = 7
tiempoDos = 4.5
distanciaTres = 791
velocidad = int(input("Teclea la velocidad a la que viaja el auto:"))

distanciaUno = tiempoUno * velocidad
distanciaDos =  tiempoDos * velocidad
tiempoTres =  distanciaTres / velocidad

print("Distancia recorrida en 7 hrs:", "{:.1f}" . format(distanciaUno))    # "{:.1f}" . format SIRVE PARA MARCAR
                                                                         #  EL NUMERO DE DECIMALES QUE QUIERES
print("Distania recorrida en 4.5hrs:", "{:.1f}" . format(distanciaDos))
print("Tiempo para recorrer 791 km:", "{:.1f}" . format(tiempoTres))
