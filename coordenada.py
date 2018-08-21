# Autor: Mariana Caballero, A01376544
#Descripción: A continuación voy a crear un programa que me ayude a calcular la distancia entre 2 puntos


#Programa

x1 = int (input("Coordenada en X del punto A:"))
y1 = int (input("Coordenada en Y del punto A:"))
x2 = int (input("Coordenada en X del punto B:"))
y2 = int (input("Coordenada en Y del punto B:"))

distancia = (((x2-x1)**2)+((y2-y1)**2))**.5

print ("Distancia: %5.4f"  %(distancia))
