#   Ejercicio python 3 Miercoles 27-04
#   IF= SE UTILIZA PARA REALIZAR UNA PREGUNTA EN UN PROGRAMA
#   INGRESO DE DATOS POR TECLADO


#   LIMPIAR PANTALLA
from os import system;
system  ("cls")


#DECLARACION DE VARIABLES
EEdad    =   int(input("Ingrese Edad :   "))

#INGRESO DE DATOS

if (EEdad >= 1 and EEdad < 12):
    print   ("A ud se le considera Niño y tiene : ",EEdad, "Años")
    print   ("===================================")
print   ("")

if (EEdad >= 12 and EEdad < 18):
    print   ("A ud se le considera Adolescente y tiene : ",EEdad, "Años")
    print   ("==========================================")
print   ("")

if (EEdad >= 18 and EEdad < 21):
    print   ("A ud se le considera Juvenil y tiene : " ,EEdad, "Años")
    print   ("======================================")
print   ("")

if (EEdad >= 21 and EEdad < 65):
    print   ("A ud se le considera Adulto y tiene : " ,EEdad, "Años")
    print   ("=====================================")
print   ("")

if (EEdad >= 65 and EEdad < 99):
    print   ("A ud se le considera Adulto Mayor y tiene : " ,EEdad, "Años")
    print   ("===========================================")
print   ("")