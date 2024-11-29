
from os import system;
system("cls");

print   ("");
print   ("DETERMINAR SI ES MAYOR DE EDAD Y JORNADA")
print   ("========================================")
print   ("")

#Ingreso de datos

Rutt    =   input("Ingrese su rut......:")
Nomm    =   input("Ingrese su nombre...:")
Edad    =   int(input("Ingrese su edad.:"))
Carr    =   "";
Jornada =   "";
print("");

#Pregunta si EDAD es mayor a 21 años,carrera y jornada

if(Edad >= 21):
    EdadIngresada= "Usted es menor de edad";
    CarrU= input("Ingrese su carrera universitaria es:");
    Jorna= input("Ingrese su jornada de estudio es...:");

    if ( CarrU =="Informatica"  or CarrU == "informatica" or CarrU == "INFORMATICA"):        
        Carr= "Pertenece a la carrera de informatica"

        if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "mañana"):        
            Jornada= "Estudia en la mañana"

        elif ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "tarde"):        
            Jornada= "Estudia en la tarde"
        
        elif ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "noche"):        
            Jornada= "Estudia en la noche"

    elif ( CarrU =="Cocina"  or CarrU == "cocina" or CarrU == "COCINA"):        
        Carr= "Ud pertenece a la carrera de cocina"

        if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "mañana"):        
            Jornada= "Estudia en la mañana"

        elif ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "tarde"):        
            Jornada= "Estudia en la tarde"
        
        elif ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "noche"):        
            Jornada= "Estudia en la noche"

else:
    EdadIngresada= "Usted es menor de edad";
    CarrU= input("Ingrese su carrera universitaria es:");
    Jorna= input("Ingrese su jornada de estudio es...:");

    if ( CarrU =="Informatica"  or CarrU == "informatica" or CarrU == "INFORMATICA"):        
        Carr= "Pertenece a la carrera de informatica"

        if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "mañana"):        
            Jornada= "Estudia en la mañana"

        elif ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "tarde"):        
            Jornada= "Estudia en la tarde"
        
        elif ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "noche"):        
            Jornada= "Estudia en la noche"

    elif ( CarrU =="Cocina"  or CarrU == "cocina" or CarrU == "COCINA"):        
        Carr= "Ud pertenece a la carrera de cocina"

        if ( Jorna =="MAÑANA"  or Jorna == "Mañana" or Jorna == "mañana"):        
            Jornada= "Estudia en la mañana"

        elif ( Jorna =="TARDE"  or Jorna == "Tarde" or Jorna == "tarde"):        
            Jornada= "Estudia en la tarde"
        
        elif ( Jorna =="NOCHE"  or Jorna == "Noche" or Jorna == "noche"):        
            Jornada= "Estudia en la noche"

print("")
print (".........Ingreso de datos.........");
print ("==================================");
print ("Su rut.....................:", Rutt);
print ("Su nombre es...............:", Nomm);
print ("Su edad es.................:", Edad);
print ("Usted pertenece a..........:", EdadIngresada);
print ("Tu carrera es..............:", Carr);
print ("Tu jornada de estudio es...:", Jornada);
print ("==================================");
