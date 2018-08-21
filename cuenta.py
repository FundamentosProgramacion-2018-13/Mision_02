# Autor: Diego Armando Ayala Hernández A01376727
# Descripcion: Este Programa te ayuda a sacar el iva y propina de una comida, Primero pide el costo. Despues multiplica por .13 y .15 pra sacar propina e iva y por ultimo suma el costo, iva y propina para sacar el total
# Escribe tu programa después de esta línea.
costo=input("Dame el costo de la comida: ")
subtotal=int(costo)

iva=subtotal*.15
propina=subtotal*.13
total =subtotal+iva+propina
print("Subtotal: $",subtotal)
print("IVA: $ ", iva)
print("Propina: $", propina)
print("Total: $", total)
