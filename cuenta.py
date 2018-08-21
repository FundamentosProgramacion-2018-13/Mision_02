# Autor: Carlos Alberto Reyes Ortiz
# Descripcion: Te ayuda a saber cuanta propina y IVA va a ser de tu comida. Dando como propina un 13% y un IVA de 15% 

# Escribe tu programa después de esta línea.
costoComida = int(input("Costo de su comida:"))
porcentajePropina = 13
porcentaheIVA = 15

propina = costoComida*porcentajePropina/100
iVA = costoComida*porcentaheIVA/100
totalPagar = costoComida + propina + iVA

print("Propina:$", "{:.2f}" . format(propina))
print("IVA:$", "{:.2f}" . format(iVA))
print("Total a pagar:$", "{:.2f}" . format(totalPagar))

