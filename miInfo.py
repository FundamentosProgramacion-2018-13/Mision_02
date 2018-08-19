#Autor: Alex Serrano Durán, A01376364
#Descripcion: Este programa recibe información del usuario y la imprime de forma organizada

nombre = str(input("Escribe tu nombre: "))
matricula = str(input("Escribe tu matrícula: "))
carrera = str(input("Escribe la carrera que estás cursando: "))
programaPrepa = str(input("Escribe tu programa en PrepaTec: "))
descripcion = str(input("Descríbete en tres oraciones (incluye gustos, hablidades, deportes que practicas, etc.): "))

print("""Nombre:
%s
Matrícula:
%s
Carrera:
%s
Programa de PrepaTec:
%s
Descripción:
%s  
""" % (nombre, matricula, carrera, programaPrepa, descripcion))
