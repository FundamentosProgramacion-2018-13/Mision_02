# Autor: Jonathan Sanabria Rocha, A01746763
# Descripcion: Problema de auto con formula v=d/t , uso de format.

# Escribe tu programa después de esta línea.
velocidad= float(input("Dame la velocidad del auto en km/h:"))
tiempo= float(input("Dame el tiempo de recorrido del auto en horas:"))
distancia=(float(velocidad)/float(tiempo))
tiempo1= input("Dame el tiempo de recorrido del auto en horas: ")
distancia1=(float(velocidad)/float(tiempo1))
distancia2=input("Dame la distancia que recorrera el auto: ")
tiempo2=(float(distancia2)/float(velocidad))
print("Velocidad del auto en km/h= ",format(velocidad,".1f")+" km/h")
print("Distancia recorrida en "+str(float(tiempo))+" hrs:=",format(distancia,".1f")+" km")
print("Distancia recorrida en "+str(float(tiempo1))+" hrs:=",format(distancia1,".1f")+" km")
print("Tiempo para recorrer "+str(float(distancia2))+" km:=",format(tiempo2,".1f")+" hrs")
