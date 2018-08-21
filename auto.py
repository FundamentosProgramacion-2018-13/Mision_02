# Autor: Diego Armando Ayala Hernández A01376727
# Descripcion: despues de obtener la velocidad de un auto. multiplica y divide para sacar la distancia que haría en 7 y 4.5 horas. Así como el tiempo que tardaria en recorrer en 791 km

# Escribe tu programa después de esta línea.
velocidad=input("¿Cuál es la velocidad del carro?")
vel=int(velocidad)
distancia1=vel*7
distancia2=vel*4.5
tiempo = 791/vel
print(" La distancia que recorrería en 7 horas es:", distancia1)
print(" La distancia que recorrería en 4.5 horas es: %0.2f" %(distancia2))
print(" el tiempo que tardara para recorrer 791 kilómetros es:", tiempo)
