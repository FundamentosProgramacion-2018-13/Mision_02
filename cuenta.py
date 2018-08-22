# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
Subtotal = int(input("Introduzca el costo de su comida"))
IVA= Subtotal*.13
Propina= Subtotal*.15
Total= Subtotal+IVA+Propina
print("Costo de su comida:",Subtotal)
print("La propina es:", Propina)
print("El IVA es:",IVA)
print("Su total a pagar es:",Total)
