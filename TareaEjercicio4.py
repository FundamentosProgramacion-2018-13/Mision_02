# Autor: Roberto Emmanuel González Muñoz A01376803
# Este programa promedia y imprime el total de alumnos de una institución.

#El usuario introduce el numero de mujeres y hombres
mujeres = int(input("Introdusca el número de mujeres: "))
hombres = int(input("Introdusca el número de hombres: "))

#Variables Globales
ToAlumnosI = mujeres + hombres
PorMujeres = mujeres*100/ToAlumnosI
PorHombres = hombres*100/ToAlumnosI

#Salida
print("Número de mujeres: ",mujeres)
print("NÚmero de hombres: ",hombres)
print("Total de alumnos inscritos: ",ToAlumnosI)
print("Porcentaje de Mujeres: ", format(PorMujeres,".1f"),"%")
print("Porcentaje de Hombres: ",format(PorHombres,".1f"),"%")