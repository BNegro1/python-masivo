#EJERCICIO 1 PYTHON IF - ELSE 05-04
#la instruccion if-else evalua dos opciones v y f
#lo primero que realiza esta instruccion es evaluar la opcion 
#verdadera del if, y si esta opcion no se cumple, recien pasa a ejecutar el else
#Programa que determina si es mayor de edad
#21 años hacia arriba es mayor de edad
#Datos a considerar: Rut, Nombre, Edad

from os import system;
("cls");

print   ("");
print   ("...Determinar si la persona es mayor de edad...")
print   ("_______________________________________________")
print   ("")

#Ingreso de datos
Rutt=   input("Ingrese su rut:.....")
Nomm=   input("Ingrese su nombre:..")
Edad=   int(input("Ingrese su edad:"))
print   ("");

#Pregunta si EDAD es mayor a 21 años
if(Edad >= 21):
    EdadIngresada=  "Usted es mayor de edad";
else:
    EdadIngresada= "Usted es menor de edad";

print("")
print ("Ingreso de datos");
print ("________________");
print ("Ingrese su rut:   ", Rutt)
print ("Ingrese su nombre:", Nomm)
print ("Ingrese su edad:  ", Edad)
print ("Usted es:", EdadIngresada)
print("")