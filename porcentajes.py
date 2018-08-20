# Autor: Luis Rcardo Chagala Cervantes, A01376951
# Descripcion: 
#1.	Leer mujeres inscritas.
#2.	Leer hombres inscritos.
#3.	Sumar hombres y mujeres inscritos.
#4.	Multiplicar (mujeres por 100) y dividir entre la suma de hombre y mujeres.
#5.	Multiplicar (hombres por 100) y dividir entre la suma de hombre y mujeres.
#6.	Imprimir Total de personas inscritas.
#7.	Imprimir porcentaje de mujeres.
#8.	Imprimir porcentaje de hombre.


# Escribe tu programa después de esta línea.
m = int(input("Mujeres Inscritas: "))
h = int(input("Hombres Inscritos: "))

totaldeinscritos = m + h
porcentajesmujeres = (m * 100) / totaldeinscritos
porcentajehombres = (h * 100) / totaldeinscritos

print ("Total de Inscritos = " , totaldeinscritos)
print ("Porcentaje de mujeres = %3.2f" % (porcentajesmujeres))
print ("Porcentaje de hombres = %3.2f" % (porcentajehombres))
