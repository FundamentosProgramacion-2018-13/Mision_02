# Autor: Jonathan Sanabria Rocha, A01746763
# Descripcion: Cuenta de un restaurante, propina e IVA.

# Escribe tu programa después de esta línea.
subtotal= float(input("Dame el subtotal de la cuenta de la comida: "))
porprop=.13
iva=.15
prop=subtotal*porprop
totiva=subtotal*iva
total=subtotal+prop+totiva
print("Costo de su comida: %s" %(subtotal))
print("Propina: "+str(float(prop)))
print("Iva: "+str(float(totiva)))
print("TOTAL: "+str(float(total)))
