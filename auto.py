# Autor: Alberto Contreras Torres, A01748151
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Escribe un programa que pregunte al usuario la velocidad a la que viaja un auto (km/h) y calcule e imprima lo siguiente:
•	La distancia en km. que recorre un cohe en 7 hrs.
•	La distancia en km. que recorre un coche en 4.5 hrs.
•	El tiempo en horas que requiere un cohce para recorrer 791 km.


# Escribe tu programa después de esta línea.
v= int(input("teclea velocidad :"))
d7= v*7
d4= v*4.5
t791km= 791/v
print("Velocidad del auto en km/h", v,"km/h")
print("Distancia recorrida en 7hr = %0.1f"% d7,"km")
print("Distancia recorrida en 4.5hr = %0.1f"% d4,"km")
print("Tiempo para recorre 791km = %0.1f"% t791km,"hr")
