#   Ejercicio python °2 Miercoles 13-04
#   Calculo de promedio
#   INGRESO DE DATOS POR TECLADO

#   LIMPIAR PANTALLA
from os import system;
system  ("cls")

#DECLARACION DE VARIABLES
Rut=    "";
Nombre= "";
Asig=   "";
N1= 0;
N2= 0;
N3= 0;
PROM=   0;
Situacion=  "";

#Ingreso de datos

print   (""); # IMPRIME UNA LINEA EN BLANCO
print   ("INGRESO DE DATOS")
print   ("----------------")
print   ("")

Rut=    input("Ingrese el rut del alumno..................:")
Nombre= input("Ingrese el nombre del alumno...............:")
Asig=   input("Ingrese la asignatura del alumno...........:")
N1= int(input("Ingrese Nota N1 del alumno.................:"))
N2= int(input("Ingrese Nota N2 del alumno.................:"))
N3= int(input("Ingrese Nota N3 del alumno.................:"))
Sueldo= "";
SueldoLiquido= "";

print   ("")
print   ("")

#Calculo de Promedio 
PROM=   (   N1  +   N2  +   N3   )  /3
#Calculo de Promedio

#Calculo de la situacion
if (PROM >= 10 and PROM < 40) :
    Situacion=  "Reprobado;"

if (PROM >= 40 and PROM < 50) :
    Situacion=  "Aprobado;"

if (PROM >= 50 and PROM < 70) :
    Situacion=  "Eximido;"

print   ("MUESTRA DE DATOS")
print   ("================")

print   ("")
print   ("ingrese rut del alumno.........:", Rut)
print   ("ingrese nombre del alumno......:", Nombre)
print   ("ingrese asignatura del alumno..:", Asig)
print   ("la nota 1 es...................:", N1)
print   ("la nota 2 es...................:", N2)
print   ("la nota 3 es...................:", N3)
print   ("promedio final es..............:", PROM)
print   ("la situacion del alumno es.....:", Situacion)