# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripcion: Calcular el total de una cuenta contando la propina y el iva. Esto a partir del subtotal indroducido por el usuario.

# Escribe tu programa después de esta línea.

sub=float(input("¿Cuanto fue el total de la comida? "))
p= sub*0.13
i= sub*0.15
total= sub + i + p

print("Costo de su comida: ",sub)
print("Propina: %0.2f" %(p))
print("IVA: %0.2f" %(i))
print("Total a pagar: %0.2f"%(total))
