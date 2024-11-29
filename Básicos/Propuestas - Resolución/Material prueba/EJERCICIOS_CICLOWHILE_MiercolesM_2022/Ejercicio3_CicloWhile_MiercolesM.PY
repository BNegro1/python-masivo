#EJERCICIO 3 CICLO WHILE 25-05-22
#Realice un programa  que calcule el prmedio de notas para 3 alumnos
#Datos a considerar
#Rut, Nombre,Nota1,Nota2,Nota3, Promedio y Situacion
#Imprimir todos los datos

from os import system
system ("cls")

Rutt= ""; 
Nomb= ""; 
Nota1= 0; 
Nota2= 0; 
Nota3= 0; 
Prom= 0; 
Situacion= ""; 

A=1
while (A <=3):
    print ("")
    print (".......INGRESO DE DATOS N°",A,"......."); 
    print ("================================="); 

    Rut= input("Ingrese su rut es.......:"); 
    Nomb= input("Ingrese su nombre es...:"); 
    Nota1= int(input("Ingrese Nota 1.........:")); 
    Nota2= int(input("Ingrese Nota 2.........:")); 
    Nota3= int(input("Ingrese Nota 3.........:")); 

    #CALCULO DE PROMEDIO

    Prom= (Nota1 + Nota2 + Nota3) /3; 

    #CALCULO DE LA SITUACION
    if (Prom >=10 and Prom < 40):
        Situacion= "Ripley"

    if (Prom >=40 and Prom < 50):
        Situacion= "Aprobado"

    if (Prom >=50 and Prom <= 70):
        Situacion= "Eximido"

    print ("")
    print ("..........MUESTRA DE DATOS N°",A,".........."); 
    print ("===================================="); 
    print ("El rut del alumno es....:", Rut);   
    print ("El Nombre del alumno es.:", Nomb); 
    print ("La nota 1 es............:", Nota1); 
    print ("La nota 2 es............:", Nota2); 
    print ("La nota 3 es............:", Nota3); 
    print ("Su promedio es..........:", Prom); 
    print ("Su situacion es.........:", Situacion); 
    print ("==================================="); 
    print ("")

    A= A+1

print (""); 
print ("fuera de el ciclo while");    
print ("")