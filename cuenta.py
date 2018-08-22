# Autor: Daniel Córdova Bermúdez, A01377242
# Descripcion: El programa calcula la propina, iva y el total del consumo.

# Escribe tu programa después de esta línea.

subtotal = float(input("Total del consumo:"))

propina = subtotal*0.13
iva = subtotal*0.15
total = subtotal+propina+iva
                 
print("Costo de su comida:",subtotal)
print("Propina:",propina)
print("IVA:",iva)
print("Total a pagar:",total)
