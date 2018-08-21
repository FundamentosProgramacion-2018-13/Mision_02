H = int(input("Hombres inscritos: "))
M = int(input("Mujeres inscritas: "))

total = H + M
porcentajeH = H * 100/total
porcentajeM = M * 100/total

print("Total de inscritos: ",total)
print("Porcentaje de mujeres: ",porcentajeM,"%")
print("Porcentaje de Hombres: ",porcentajeH,"%")