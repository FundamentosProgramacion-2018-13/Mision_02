# Autor: Ithan Alexis Pérez Sánchez, A01377717
# Descripcion: Calcular el costo total de una comida, incluyendo propina e IVA

# Escribe tu programa después de esta línea.
Comida = int(input("Costo de tu comida es de: $"))

Propina = 0.13 * Comida
IVA = 0.15 * Comida
Saldo_a_cubrir = Comida + Propina + IVA

print ("Propina de: $", Propina)
print ("IVA de: $", IVA)
print ("Su Costo Total es de: $", Saldo_a_cubrir)
