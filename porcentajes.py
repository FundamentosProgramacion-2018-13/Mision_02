# Autor: Jocelyn López Ortíz, A01377451
# Descripcion: Cálculo de porcentaje de hombres y mujeres inscritos

# Escribe tu programa después de esta línea.
nummujeres = int(input("Mujeres inscritas: "))
numhombres = int(input("Hombres inscritos: "))

total = numhombres + nummujeres
porcentajem= nummujeres / total * 100
porcentajeh= numhombres / total * 100

print("Total de inscritos," , total)
print("Porcentaje de mujeres: ", round(porcentajem,1), "%")
print("Porcentaje de hobmbres: ", round(porcentajeh,1), "%")

