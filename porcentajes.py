# Autor: Rodolfo Anibal Altamirano Sánchez     A01377949
# Descripcion: se te proporcionan los datos de cantdad de hombres y mujeres que hay en una clases y se necesita calcular el total y el porcentaje de cada genero

# Escribe tu programa después de esta línea.
hombres = int(input("Cantidad de Hombres:"))
mujeres = int(input("Cantidad de mujeres:"))
total = hombres + mujeres
porcentajeH = (hombres*100)/total
porcentajeM = 100-porcentajeH

print("Alumnos inscritos:",total)
print("Porcentaje de hombres %.2f"%porcentajeH,"%")
print("Porcentaje de mujeres %.2f"%porcentajeM,"%")
