# Autor: Jocelyn López Ortíz, A01377451
# Descripcion: Cálculo del costo de una comida considerando propina e IVA

# Escribe tu programa después de esta línea.
costo = int(input("Costo de su comida: "))

subtotal = costo
propina = costo*0.13
IVA = costo*0.15
total = subtotal+propina+IVA

print("Propina: $" , propina)
print("IVA: $", IVA)
print ("Total a pagar: $", total)
