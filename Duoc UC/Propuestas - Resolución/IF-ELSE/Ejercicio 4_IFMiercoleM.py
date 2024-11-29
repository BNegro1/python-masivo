#   Ejercicio python 3 Miercoles 27-04
#   IF= SE UTILIZA PARA REALIZAR UNA PREGUNTA EN UN PROGRAMA
#   INGRESO DE DATOS POR TECLADO


#   LIMPIAR PANTALLA
from os import system
system  ("cls")


#DECLARACION DE VARIABLES
print ("")
print ("...INGRESE GENERO DE LA PERSONA...");
print ("==================================")
print ("")

#INGRESO DE DATOS
Persona = input("Ingrese genero de la persona   :")
print ("")

if (Persona ==  "HOMBRE"    or Persona == "hombre" or Persona == "Hombre"):
    print ("La persona ingresada es :..............................:", Persona);
    Rut =   input("Ingrese su rut..................................:");
    Nombre  =   input("Ingrese su Nombre...........................:");
    SueldoBase  =   int(input("Ingrese su Sueldo Base..............:"));
    Bono =   int(input("Ingrese Bono...............................:"));
    Anticipo    =   int(input("Ingrese su anticipo.................:"));

 #DEBE CALCULAR EL SUELDO: LIQUIDO (SBASE + BONO) - (ANTICIPO)
    Sueldoliquido = (SueldoBase + Bono) - (Anticipo)

    print ("");
    print ("...MUESTREO DE DATOS...");
    print ("======================");
    print ("La persona Ingresada es....................................:", Persona);
    print ("El rut de la persona es....................................:", Rut);
    print ("El nombre de la persona es.................................:", Nombre);
    print ("El sueldo base ingresado es................................:", SueldoBase);
    print ("El bono ingresado es.......................................:", Bono);
    print ("El anticipo ingresado es...................................:", Anticipo);
    print ("El sueldo liquido de la persona es.........................:", Sueldoliquido);
    print ("============================================================");

if (Persona ==  "MUJER"    or Persona == "mujer" or Persona == "Mujer"):
    print ("La persona ingresada es :.................................:", Persona);
    Rut = input("Ingrese su rut.......................................:");
    Nombre =   input("Ingrese su Nombre...............................:");
    Direccion  =   input("Ingrese su Direccion........................:");
    Edad =  input ("ingrese edad......................................:")
    

    print ("");
    print ("...MUESTREO DE DATOS...");
    print ("======================");
    print ("La persona Ingresada es.....................................:",Persona);
    print ("El rut de la persona es.....................................:",Rut);
    print ("El nombre de la persona es..................................:",Nombre);
    print ("La edad de la persona es....................................:",Edad);
    print ("============================================================"); 

if (Persona != "HOMBRE" or Persona != "hombre" or Persona != "Hombre" or Persona != "MUJER" or Persona != "mujer" or Persona != "Mujer"):
    print ("...ERROR, este tipo de genero es incorrecto!...");
    print ("");