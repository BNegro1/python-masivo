
from os import system
system ("cls")

print ("")
print ("EJERCICIO 1 GUIA 2 ")
print ("===================")
print ("")

print ("CALCULO DE PROMEDIO")
print ("")

Rutt=  ""; 
Nomb=  ""; 
Asig=  ""; 
Carr=  ""; 
CarrU= ""; 
Nota1=  0; 
Nota2=  0; 
Nota3=  0; 
Prom=   0; 
Examen= 0; 

Rutt= input ("Ingrese su rut..........................:"   )
Nomb= input ("Ingrese su nombre.......................:"   )
Asig= input ("Ingrese su asignatura...................:"   )
Nota1= int(input("Ingrese su nota 1.....................:"))
Nota2= int(input("Ingrese su nota 2.....................:"))
Nota3= int(input("Ingrese su nota 3.....................:"))
Examen= int(input("Ingrese su calificacion en el examen:" ))

#CALCULOS/PROCESOS
Prom= (Nota1 + Nota2 + Nota3) /3
Examen25= (Examen * 25) /100
Prom75= (Prom * 75) /100
PromF= (Prom75 + Examen25)

if (PromF >= 10 and Prom < 40):
    Situacion=  "Reprobado;"

elif (PromF >= 40 and Prom < 50):
    Situacion=  "Aprobado;"

else: 
    (PromF >= 50 and Prom < 70)
    Situacion=  "Eximido;"

print("")
print (".............Ingreso de datos..........."); 
print ("========================================"); 
print ("Su rut es..................:",       Rutt); 
print ("Su nombre es...............:",       Nomb); 
print ("Nota 1.....................:",      Nota1); 
print ("Nota 2.....................:",      Nota2); 
print ("Nota 3.....................:",      Nota3); 
print ("Nota examen................:",     Examen); 
print ("Tu promedio es.............:",       Prom); 
print ("Tu situacion es............:",  Situacion); 
print("")