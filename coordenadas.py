#Autor: Luis Mario Cervantes Ortiz , A01376958

#Descripción Se va a saber la distancia que hay desde una cordenada (x1,y1) a (x2,y2)


x1=input("Coordenada x1= ")
y1=input("Coordenada y1= ")
x2=input("Coordenada x2= ")
y2=input("Coordenada y2= ")

x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)
Distancia=((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("Distancia: %.4f" % Distancia)