# Autor: Ithan Alexis Pérez Sánchez, A01377717
# Descripcion: Calcular la estimación total de alumnos inscritos y el porcentaje que representa Hombres y Mujeres

# Escribe tu programa después de esta línea.
Female = int(input("Mujeres Inscritas: "))
Male = int(input("Hombres Inscritos: "))

Total_de_Alumnos = Female + Male
ProcentajeH = Male * 100 / Total_de_Alumnos
ProcentajeM = Female * 100 / Total_de_Alumnos

print("Procentaje de mujeres que hay: ", ProcentajeM, "%")
print("Porcentaje de hombre que hay: ", ProcentajeH, "%")
print("Este es el Total de Inscritos: ", Total_de_Alumnos)
