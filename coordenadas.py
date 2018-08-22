# Autor: María Fenanda Vela Calderón, A01377958
# Descripcion: Calcular distancia entre dos puntos.

# Escribe tu programa después de esta línea.

x1 = int( input( "Escribe x1: "))
y1 = int( input( "Escribe y1: "))

x2 = int( input( "Escribe x2: "))
y2 = int( input( "Escribe y2: "))

d = ( ( x2 - x1 )**2 + ( y2 - y1 )**2 ) **(1/2)

print( "x1:", x1)
print( "y1:", y1)
print( "x2:", x2)
print( "y2:", y2)
print ("La distacia entre los puntos es: %9.04f" % d)
