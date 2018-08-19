# Autor: luisJonathanRosasRamos, A01377942
# Descripcion: Con el costo total relizar una nueva operacion, sumandole el IVA y propina

# Escribe tu programa después de esta línea.

TotalComida = float(input("Cuanto fue el total de la comida: "))

propina = TotalComida*0.13

IVA = TotalComida*0.15

print("El subtotal: ", TotalComida)
print("La propina es de: ", propina)
print("El Iva es de: ", IVA)
print("El total a pagar es de: ", TotalComida+propina+IVA)
