# Autor: Zabdiel Valentin Garduño Vivanco, A01377950
# Descripcion: Sacar la distancia de entre dos puntos dados en una recta.

# Escribe tu programa después de esta línea

x1= int(input("x1: "))
x2= int(input("x2: "))
y1= int(input("y1: "))
y2= int(input("y2: "))

eX=(x2-x1)**2
eY=(y2-y1)**2
d=(eX+eY)**(1/2)

print("Distancia:  %.4f" %(d))


