TotalComida = float(input("Cuanto fue el total de la comida: "))

propina = TotalComida*0.13

IVA = TotalComida*0.15

print("El subtotal: ", TotalComida)
print("La propina es de: ", propina)
print("El Iva es de: ", IVA)
print("El total a pagar es de: ", TotalComida+propina+IVA)

