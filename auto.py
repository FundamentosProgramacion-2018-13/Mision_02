# Autor: María Fenanda Vela Calderón, A01377958
# Descripcion: Calcular distancia y tiempo que viaja el auto

# Escribe tu programa después de esta línea.

v = int( input( "Escribe la velocidad del auto: " ))

r1 = v*7     #Recorrido 1

r2 = v*4.5     #Recorrido 2

t = 791/v

print( "En 7hrs el auto recorrió: %5.01f km"  % r1 )
print( "En 4.5hrs el auto recorrió:  %5.01f km" % r2)
print( "Para recorrer 791km el auto tardó: %5.01f h" % t)
