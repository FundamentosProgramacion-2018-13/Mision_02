# Autor: Arturo Márquez Olivar, A01376086
# Descripcion: Imprime resultados de distancias solicitadas en el problema 2.

# Escribe tu programa después de esta línea.

v= input("¿Con qué velocidad viajó el auto?")

  v2= v*(5/18)
  t1= 7*3600
  t2= 4.5*3600
  d3= 791*1000
  
  d1= v2*t1
  d2= v2*t2
  t3= d3/v2
  
  t4= t3/3600
  d4= d1/1000
  d5= d2/1000
 
print("En 7hrs. el auto recorrió: ", d4)
print("En 4.5hrs. el auto recorrió: ", d5)
print("El tiempo que el auto necesita para llegar a 791km, es de: ", t4)
