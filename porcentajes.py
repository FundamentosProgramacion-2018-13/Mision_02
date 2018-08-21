# Autor: Jose LuiS Mata Lomeli, A01377205 
# Descripcion: Dar el porcentaje de alumnos y alumnas de un grupo.

# Escribe tu programa después de esta línea.

Alumnos_morras= int(input("Escriba la cantidad de alumnas inscritas: ")) 
Alumnos_morros= int(input("Escriba la cantidad de alumnos inscritos: "))

Total_Alumnos= Alumnos_morras + Alumnos_morros

Porcentaje_Femm= (Alumnos_morras*100)/Total_Alumnos
Porcentaje_Masc= (Alumnos_morros*100)/Total_Alumnos

print("Total de inscritos: ", (Total_Alumnos))
print("Porcentaje de Alumnas: ", (Porcentaje_Femm))
print("Porcentaje de Alumnos: ", (Porcentaje_Masc))


