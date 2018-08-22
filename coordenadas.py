# Autor: Daniel Córdova Bermúdez, A01377242
# Descripcion:El programa calcula la distancia de las coordendas. 

# Escribe tu programa después de esta línea.

x1 = float(input("Valor X1:"))
y1 = float(input("Valor Y1:"))
x2 = float(input("Valor X2:"))
y2 = float(input("Valor Y2:"))

distancia = ((x2-x1)**2 + (y2-y1)**2)*(1/2)

print("Distancia: %.04f " %(distancia))
