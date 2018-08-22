# Autor: Alberto Contreras Torres, A01748151
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Escribe un programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.
o	El número total de alumnos inscritos.
o	El porcentaje de mujeres.
o	El porcentaje de hombres.

# Escribe tu programa después de esta línea.
a= int(input("Teclea No. mujeres :"))
b= int(input("Teclea No. hombres :"))
ta= a+b
pm= a*100/ta
ph= b*100/ta
print("Total de inscritos :",ta)
print("Porcentaje de mujeres = %0.1f"% pm,"%")
print("Porcentaje de hombres = %0.1f"% ph,"%")
