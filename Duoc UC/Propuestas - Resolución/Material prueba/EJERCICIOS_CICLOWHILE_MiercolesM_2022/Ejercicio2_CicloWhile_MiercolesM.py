#EJERCICIO 2 CICLO WHILE 25-05-22
#Imprimir los numeros del 1 al 10 de 1 en 1
#Imprimir el acumulado de cada procesos
#Imprimir el acumulado de los procesos 1 al 5
#Imprimir el acumulado de los procesos 6 al 10
#Imprimir el total acumulado despues de los 10 procesos realizados

from os import system
system ("cls")

#Inicializacion de Variables
A=0
AcumP=0
ContP=0
ContP15=0
ContP610=0
AcumP15=0
AcumP610=0

print (""); 
print ("...Ciclo repetitivo While..."); 
print ("============================"); 
print ("");  

A= 1;  

while (A <= 10):
    AcumP= AcumP + A; 
    print ("El proceso realizado es.........:", A); 
    print ("El Acumulado de cada proceso es.:", AcumP); 
    print ("")
    ContP= ContP+1

    if(ContP <= 5):
        ContP15 = ContP15+1
        AcumP15 = AcumP15+A 
    
    elif(ContP > 5 and ContP <= 10):
        ContP610 = ContP610+1
        AcumP610 = AcumP610+A 
    A= A+1; 

print (""); 
print ("Opcion fuera de while");    
print ("")

print("..................MUESTRA DE DATOS.................."); 
print ("===================================================");  
print ("El total final de procesos acumulado es.:", AcumP); 
print ("El total de procesos del 1 - 5 es.......:", ContP15); 
print ("El proceso acumulado del 1 - 5 es.......:", AcumP15); 
print ("==================================================="); 
print ("El total de procesos del 6 - 10 es......:", ContP610); 
print ("El proceso acumulado del 6 - 10 es......:", AcumP610); 
print ("==================================================="); 
print ("")


