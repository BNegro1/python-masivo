#EJERCICIO 1 IF-ELSE
#COMO SE REALIZA UN PREGUNTA EN PYTHONQUE TENGA DOS ALTERNATIVA
#IF = SE UTILIZA PARA REALIZA UNA PREGUNTA EN UN PROGRAMA
#ELSE = SE UTILIZA CUANDO LA PREGUNTA TIENE 2 OPCIONES O 2 ALTERNATIVAS


#   LIMPIAR PANTALLA
from os import system;
system  ("cls")

print ("")
print ("=========")
print ("Autor.....:")
print ("Programa..:")
print ("Fecha.....:")
print ("")

EEdad =  int(input("Ingrese Edad...:"))
print ("La edad es:", EEdad, "Años")

if (EEdad >=21):
    print ("La Persona es mayor de edad")
else:
    print ("La persona es Menor de edad")

print ("")
print ("================")
print ("FIN DEL PROGRAMA")
print ("================")
print ("")