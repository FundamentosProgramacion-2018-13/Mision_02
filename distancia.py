# Autor: David Rodriguez Fragoso, A01748760
# Descripcion: Problema 5

# Escribe tu programa después de esta línea.

#d= distancia

x1 = int(input("Dame x1: "))
y1 = int(input("Dame y1: "))
x2 = int(input("Dame x2: "))
y2 = int(input("Dame y2: "))

d = (((x2-x1)**2)+((y2-y1)**2))**0.5

print ("x1: ", x1)
print ("y1: ", y1)
print ("x2: ", x2)
print ("y2: ", y2)
print ("La distancia es: %4.4f"% (d))
