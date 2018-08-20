# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
mujeresI = int(input("No. de mujeres inscritas: "))
hombresI = int(input("No. de hombres inscritos: "))

total = mujeresI + hombresI
mujeresP = float(mujeresI / total * 100)
hombresP = float(hombresI / total * 100)

print("""Total de personas inscritas: %d
Porcentaje de mujeres: %.01f porciento 
Porcentaje de hombres: %.01f porciento """
      %(total,mujeresP,hombresP))
