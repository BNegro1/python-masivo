#EJERCICIO 1 PYTHON IF - ELSE 05-04
#la instruccion if-else evalua dos opciones v y f
#lo primero que realiza esta instruccion es evaluar la opcion 
#verdadera del if, y si esta opcion no se cumple, recien pasa a ejecutar el else
#Programa que determina si es mayor de edad con if anidado
#Mismo programa anterior pero con if- else e if anidados
#Datos a considerar: Rut, Nombre, Edad

from os import system;
system("cls");

print   ("");
print   ("Determinar si la persona es mayor de edad")
print   ("_________________________________________")
print   ("")

#Ingreso de datos

Rutt    =   input("Ingrese su rut:......")
Nomm    =   input("Ingrese su nombre:...")
Edad    =   int(input("Ingrese su edad:"))
Carr    =   input("Ingrese su carrera:..")
Jornada ="";
print("");

#Pregunta si EDAD es mayor a 21 años

if(Edad >= 21):
    EdadIngresada=  "Usted es mayor de edad";
    Jorna= input("ingrese su jornada de estudio...:");  
    if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "MAÑANA"):        
        Jornada= "Ud estudia en la mañana"
    if ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "TARDE"):        
        Jornada= "Ud estudia en la mañana"
    if ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "NOCHE"):        
        Jornada= "Ud estudia en la mañana"

    

else:
    EdadIngresada= "Usted es menor de edad";
    Jorna= input("ingrese su jornada de estudio...:");  
    if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "mañana"):        
        Jornada= "Ud estudia en la mañana"
    if ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "tarde"):        
        Jornada= "Ud estudia en la mañana"
    if ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "noche"):        
        Jornada= "Ud estudia en la mañana"

print("")
print ("Ingreso de datos");
print ("________________");
print ("Ingrese su rut:....", Rutt)
print ("Ingrese su nombre:.", Nomm)
print ("Ingrese su edad:...", Edad)
print ("Usted es:.", EdadIngresada)
print ("Ingrese su carrera:", Carr)
print ("Ingrese su Jornada", Jornada)
print("")