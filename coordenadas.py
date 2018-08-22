# Autor: Carlos Badillo García, A01377618
# Descripcion: Usando las dos coordenadas dadas, descubrir la distancia entre ambas.

# Escribe tu programa después de esta línea.

ppx = int(input("¿Cuál es el valor de x1?"))
ppy = int(input("¿Cuál es el valor de y1?"))
spx = int(input("¿Cuál es el valor de x2?"))
spy = int(input("¿Cuál es el valor de y2?"))

d = ((spx-ppx)**2+(spy-ppy)**2)**(1/2)

print("La distancia entre los dos puntos es:", d)
