# Autor: Luis Mario Cervantes Ortiz , A01376958
# Descripcion: Se esta resolviendo el problema de saber a cuanto viaja un coche y las distancias y tiempo que se tardan en determinadas horas y kilometros respectivamente
# Escribe tu programa después de esta línea.
Velocidad=input("¿Cual es su velocidad:")

Velocidad=int(Velocidad)


formula_d= (Velocidad*7)
print("Distancia recorrida en 7 hrs:", formula_d,"km")

formula_d=(Velocidad*4.5)
print("Distancia recorrida en 4.5hrs: %5.1f"% (formula_d),"km")

formula_t=(791/Velocidad)
print("Tiempo para reccorrer 791km:%5.1f" %(formula_t),"km")
