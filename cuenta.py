# Autor: Luis Mario Cervantes Ortiz , A01376958
# Descripcion: Saber cuanto vas a pagar de total en una comida con propina y el IVA incluido

# Escribe tu programa después de esta línea.
comida= input("Costo de la comida:")
comida=int (comida)

propina= comida*.13
print ("Propina: %.2f" % propina)
iva=(comida*.15)
print("IVA:%.2f"% iva)
subtotal=(comida+propina+iva)
print("Subtotal: %.2f" % subtotal)