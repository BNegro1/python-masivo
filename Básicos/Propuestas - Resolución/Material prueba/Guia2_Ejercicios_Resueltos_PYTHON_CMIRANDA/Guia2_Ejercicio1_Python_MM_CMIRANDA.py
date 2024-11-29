
from os import system
system ("cls")

print ("")
print ("EJERCICIO 1 GUIA 2 ")
print ("===================")
print ("")

print ("CALCULO DE PROMEDIO")
print ("")

#VARIBLES
Rutt= "";
Nomb= "";
Asig= "";
Carr= "";
CarrU= "";
Nota1= 0;
Nota2= 0;
Nota3= 0;
Prom= 0;
Situacion= "";
ContR= 0;
ContA= 0;
ContE= 0;

#INGRESO DE DATOS
Rutt= input ("Ingrese su rut..........................:"   )
Nomb= input ("Ingrese su nombre.......................:"   )
Asig= input ("Ingrese su asignatura...................:"   )
Nota1= int(input("Ingrese su nota 1.....................:"))
Nota2= int(input("Ingrese su nota 2.....................:"))
Nota3= int(input("Ingrese su nota 3.....................:"))
CarrU= input("Ingrese su carrera universitaria.......:"    );

Nota1= (Nota1 * 25) /100
Nota2= (Nota2 * 35) /100
Nota3= (Nota3 * 40) /100

Prom= (Nota1 + Nota2 + Nota3)

if (Prom >= 10 and Prom < 40):
    ContR= ContR+1
    Situacion=  "Reprobado;"
    CarrU= print ("Pertenece a la carrera de informatica", CarrU);

    if ( CarrU =="Informatica"  or CarrU == "informatica" or CarrU == "INFORMATICA"):        
        Carr= "Pertenece a la carrera de informatica"

    elif  ( CarrU =="Enfermeria"  or CarrU == "enfermeria" or CarrU == "ENFERMERIA"):        
        Carr= "Pertenece a la carrera de Enfermeria"

elif (Prom >= 40 and Prom < 50):
    ContA= ContA+1
    Situacion=  "Aprobado;"

    if ( CarrU =="Informatica"  or CarrU == "informatica" or CarrU == "INFORMATICA"):        
        Carr= "Pertenece a la carrera de informatica"

    elif  ( CarrU =="Enfermeria"  or CarrU == "enfermeria" or CarrU == "ENFERMERIA"):        
        Carr= "Pertenece a la carrera de Enfermeria"

elif (Prom >= 50 and Prom < 70):
    ContE= ContE+1
    Situacion=  "Eximido;"

    if ( CarrU =="Informatica"  or CarrU == "informatica" or CarrU == "INFORMATICA"):        
        Carr= "Pertenece a la carrera de informatica"

    elif  ( CarrU =="Enfermeria"  or CarrU == "enfermeria" or CarrU == "ENFERMERIA"):        
        Carr= "Pertenece a la carrera de Enfermeria"

else:
    print ("===========================================")
    print ("ASEGURESE DE HABER RELLENADO BIEN SUS DATOS")
    print ("===========================================")

#MUESTRA DE DATOS
print("")
print ("............Ingreso de datos............."); 
print ("========================================="); 
print ("Su rut es....................:",      Rutt); 
print ("Su nombre es.................:",      Nomb); 
print ("Tu asignatura revisada es....:",      Asig); 
print ("Tu carrera es................:",      Carr); 
print ("Nota 1.......................:",     Nota1); 
print ("Nota 2.......................:",     Nota2); 
print ("Nota 3.......................:",     Nota3); 
print ("Tu promedio es...............:",      Prom); 
print ("Su situacion es..............:", Situacion); 

print ("==============================----======="); 
print ("Cantidad de eximidos.........:", ContE); 
print ("Cantidad de aprobados........:", ContA); 
print ("Cantidad de reprobados.......:", ContR); 
print ("==================================----==="); 