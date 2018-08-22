# Autor: Jocelyn López Ortíz, A01377451
# Descripcion: Cálculo de la distancia entre dos puntos ubicados en un plano cartesiano

# Escribe tu programa después de esta línea.

x1 = int(input("Valor de x1: "))
x2 = int(input("Valor de x2: "))
y1 = int(input("Valor de y1: "))
y2 = int(input("Valor de y2: "))

distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("Distancia: ", round(distancia,4))
