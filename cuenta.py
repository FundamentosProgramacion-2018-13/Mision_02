# Autor: Erick David Ramírez Martínez, A01748155
# Descripcion: Con base al costo de la comida del cliente, hay que clacular el IVA, la propina y el total. Por último imprimir el subtotal, la propina, el IVA y el total a pagar

# Escribe tu programa después de esta línea.

subtot=float(input("Introduzca el costo de la comida: "))

prop=subtot*0.13
IVA=subtot*0.15
total=subtot+prop+IVA

print("El subtotal a pagar de la comida es de: $%.2f" %(subtot))
print("La propina a pagar es de: $%.2f" %(prop))
print("El IVA a pagar es de: $%.2f" %(IVA))
print("total a pagar es de: $%.2f" %(total))
