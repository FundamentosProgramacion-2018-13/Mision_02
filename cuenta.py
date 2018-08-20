# Autor: tuNombreCompleto, tuMatricula
# Descripcion:
#1.	Leer el costo de la comida.
#2.	Calcula la propina multiplicando el costo por 13 y dividir el resultado entre 100.
#3.	Calcula el IVA multiplicando el costo por 15 y dividir el resultado entre 100.
#4.	Suma el costo de la comida más la propina más el IVA para calcular el total a pagar.
#5.	Imprime Propina.
#6.	Imprime IVA.
#7.	Imprime Total a pagar.


# Escribe tu programa después de esta línea.
Comida = int(input("Costo de su comida: "))

propina = (13 * Comida) / 100
IVA = (15 * Comida) / 100

total = Comida + propina + IVA

print ("Propina = " , propina)
print ("IVA = " , IVA)
print ("Total a pagar = " , total)
