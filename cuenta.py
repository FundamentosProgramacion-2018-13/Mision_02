# Autor: Rodolfo Anibal Altamirano Sánchez
# Descripcion: Se te da un subtotal y tu debes de calcular IVA, propina y sumarlo todo para tener un totla a pagar

# Escribe tu programa después de esta línea.
subtotal = float(input("Subtotal:"))
propina = subtotal*(0.13)
iva = subtotal*(0.15)
total = subtotal + iva + propina
print("Propina %.2f"%propina)
print("IVA %.2f"%iva)
print("Total: %.2f"%total)
