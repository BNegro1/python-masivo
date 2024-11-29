#EJERCICIO 3 VALIDAR RESTA CICLO FOR 
#ciclo repetitivo for (for = para)

#ESTOS VALORES SE DEBEN RESTAR, VALIDE LA RESTA QUE EL VALOR 1 >= AL VALOR 2 PARA PODER RESTARLOS

from os import system
system ("cls")

print ("\n\n")

#Inicializacion de variables
Val1= 0 #VARIABLE VAL 1
Val2= 0 #VARIABLE VAL 2
Resul= 0 #VARIABLE PARA EL RESULTADO

print ("...VALIDACION DE RESTAR 2 VALORES...")
print ("")

Val1= int(input("Ingrese el valor 1.:"))
Val2= int(input("Ingrese el valor 2.:"))
print("")

while(Val1 < Val2):
    print ("ERROR, el valor 1 debe ser >= al valor 2!!!") 

Resul= (Val1 - Val2)

print("....MUESTRA DE DATOS....")
print("========================")
print("El valor 1 es:", Val1)
print("El valor 2 es:", Val1)
print("El resultado de la resta de", Val1, "-", Val2, "es:", Resul)
print("========================")