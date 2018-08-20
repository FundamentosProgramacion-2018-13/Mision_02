# Autor: Zabdiel Valentin Garduño Vivanco, A01377950.
# Descripcion: Calcular el IVA, propina y total a pagar de una cuenta.

# Escribe tu programa después de esta línea

c= int(input("Teclea el costo de su comida: "))

p=c*0.13
iva=c*0.15
total=c+p+iva

print("Propina: %.2f" %(p))
print("IVA: %.2f" %(iva))
print("Total a pagar:%.2f " %(total))

