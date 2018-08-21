# Autor: Jose Luis Mata Lomeli, A01377205 
# Descripcion: Sacar la propina y el IVA del precio de una comida

# Escribe tu programa después de esta línea.

Comida= int(input("Escriba el costo de la comida: "))

Propina= Comida*0.13
IVA= Comida*0.15

Total_Pagar= Comida + Propina + IVA

print("Costo de la Comida: ", (Comida))
print("Propina: ", (Propina))
print("IVA: ", (IVA))
print("Total a pagar: ", (Total_Pagar)) 
