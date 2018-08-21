# Autor: Jesús Emmanuel Alcalá Nava, A01376766
# Descripcion: da al usuario el total de la cuenta con IVA y propina

# Escribe tu programa después de esta línea.
subtotal= float(input("costo de la comida:"))
propina= subtotal*.13
iva= subtotal*.15
total= subtotal+propina+iva
print("""
propina: $%.02f
IVA: $%.02f
total: $%.02f""" %(propina, iva, total))
