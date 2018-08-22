# Autor: Alberto Contreras Torres, A01748151
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.
Escribe un programa que calcula el costo total de una comida en un restaurante.
o	El subtotal (costo de la comida)
o	La propina.
o	El IVA.
o	El total a pagar. (Suma del subtotal, la propina y el IVA)

# Escribe tu programa después de esta línea.
a= int(input("Teclea Costo de la Comida :"))
propina= a*.13
iva= a*.15
tp= a+propina+iva
print("Costo de su comida= %0.2f $"% a)
print("Propina= %0.2f $"% propina)
print("Iva= %0.2f $"% iva)
print("Total a pagar %0.2f $"% tp)
