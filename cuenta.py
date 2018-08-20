# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
subtotal = float(input("Costo de la comida: "))

tip = subtotal * 0.13
IVA = subtotal * 0.15
total = subtotal + tip +IVA

print("""Propina: $%.02f
Cantidad de IVA: $%.02f
Total de la cuenta: $%.02f"""
      %(tip, IVA, total))
