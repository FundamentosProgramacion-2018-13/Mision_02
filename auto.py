# Autor: David Rodriguez Fragoso, A01748760
# Descripcion: Problema 2

# Escribe tu programa después de esta línea.

#t = tiempo
#v = velocidad
#d = distancia

v = int(input("¿Cuál es la velocidad del auto en km/h?: "))
d1 = v*7
d2 = v*4.5
t = 781/v

print ("Velocidad del auto en km/h: %4.1f"% (v))
print ("Distancia recorrida en 7hrs: %4.1f"% (d1), "km")
print ("Distancia recorrida en 4.5hrs: %4.1f"% (d2), "km")
print ("Tiempo para recorrer 791km: %4.1f"% (t), "hrs")
