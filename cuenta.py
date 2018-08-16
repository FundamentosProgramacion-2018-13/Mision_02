# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcular raices de una funcion cuadrada

# Escribe tu programa despues de esta linea.

"""
Analisis:
E:cuenta
S:subtotal, propina, iva, total a pagar
E/S:
subtotal = cuenta
propina = cuenta * .13
iva = cuenta * .16
total a pagar = cuenta + iva + propina

Algoritmo:
Preguntar total de cuenta a usuario y asignarlo a variable cuenta y total
Multiplicar cuenta por .13, reportar y agregar a total
Multiplicar cuenta por .16, reportar y agregar al total
Imprimir total
"""

cuenta = int(input("Costo de la comida: "))
print("Subtotal: " + str(cuenta))
total = cuenta
propina = cuenta * .13
print("Propina: " + str(propina))
total = total + propina
iva = cuenta * .16
total = total + iva
print("IVA: " + str(iva))
print("Total de la cuenta: " + str(total))