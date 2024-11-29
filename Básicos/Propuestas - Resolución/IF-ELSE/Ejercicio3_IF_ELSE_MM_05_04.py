# Ejercicio 3 IF - IF-ELSE
# EJERCICIO OPERACIONES MATEMATICAS BASICAS

from os import system
system ("cls")

print ("...OPeraciones matematicas basicas...")
print ("_____________________________")

Val1= int(input("Ingrese valor :"));
Val2= int(input("Ingrese valor :"));
Val3= int(input("Ingrese valor :"));

#Menu de opciones
print ("")
print ("..Menu de opciones..      ");
print ("====================      ");
print ("    1. Sumar valores      ");
print ("    2. Restar valores     ");
print ("    3. Multiplicar valores");
print ("    4. Divir valores      ");

Resp= int(input("Ingrese opcion (1-5):"));

# Evaluar la respuesta ingresada por el usuario
if( Resp == 1 ):
    OperaM= "Ud. a realizado una Suma de datos"
    Resultado =(Val1 + Val2 + Val3);

if( Resp == 2 ):
    OperaM= "Ud. a realizado una Resta de datos"
    Resultado =(Val1 - Val2);

if( Resp == 3 ):
    OperaM= "Ud. a realizado una Multiplicacion de datos"
    Resultado =(Val1 * Val2);

if( Resp == 4 ):
    OperaM= "Ud. a realizado una Division de datos"
    Resultado =(Val1 / Val2);

#Ingreso de datos
print("")
print ("Muestra de datos")
print ("________________")
print ("La operacion realizada es....:", OperaM)
print ("Datos a operar.........:", Val1)
print ("Datos a operar.........:", Val2)
print ("datos a operar.........:", Val3)
print ("El resultado es...........:", Resultado)
print ("")