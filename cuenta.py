# Autor: Luisa Fernanda Arellano Alvarado
# Descripcion: Facilitar el Cálculo de tu cuenta en un restaurante 

a = int(intput("Teclea costo de la comida"))
b = float(intput("Teclea porcentaje de propina))
c = float(intput("Teclea porcentaje de IVA))
                 
CostoComida = a            
Propina = (b*a)/100
IVA = (c*a)/100
ToatalApagar = CostoComida + Propina + IVA

print("Costo Comida:",CostoComida)
print("Propina:",Propina)
print("IVA:",IVA)
print("Total a pagar:",TotalApagar) 

