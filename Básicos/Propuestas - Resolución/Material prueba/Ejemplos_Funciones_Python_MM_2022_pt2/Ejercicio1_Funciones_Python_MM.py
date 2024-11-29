# Ejemplo 1 FUNCIONES
# EJEMPLO DE FUNCIONES SIN RETORNO DE VALORES O SIN RETORNO DE PARAMETROS
#

from os import system
system ("cls")

#INICIALIZACION DE VALORES
Opc=    0; #Se inicializa la variable opc que recibira las opciones del menu
Val1=   0; 
Val2=   0; 
Result= 0; 
Operacion= ""; 

print ("")
print ("EJEMPLO DE FUNCIONES")
print ("====================")
print ("")


while (Opc < 1 or Opc > 4):
    
    from os import system
    system ("cls")

    print ("... Menu de opciones basicas ...")
    print ("================================")
    print ("")
    print ("1. Sumar valores")
    print ("2. Restar valores")
    print ("3. Multiplicas valores")
    print ("4. Dividir valores")
    print ("")

    Opc= int(input("Ingrese opcion (1-4)...:"))
    print ("")

Val1= int(input("Ingrese el Valor 1.....:"))
Val2= int(input("Ingrese el Valor 2.....:"))

#Funcion MostarDatos se debe crear antes de que se utilice
def MostrarDatos ():
    print ("")
    print ("......Muestra de datos en funcion.......")
    print ("========================================")
    print ("La operacion seleccionada es....:", Operacion)
    print ("El valor 1 ingresado es.........:", Val1)
    print ("El valor 2 ingresado es.........:", Val2)
    print ("El resultado de la operacion es.:", Resul)
    print ("========================================")
    print ("")


if (Opc == 1 ):
    Operaciones = ("Ud selecciono la operacion Sumar")
    Resul = (Val1 + Val2)
    MostrarDatos(); #llama a la funcion a mostrar datos

if (Opc == 2 ):
    Operaciones = ("Ud selecciono la operacion Restar")
    while (Val1 < Val2):
        print ("\n... ERROR EL VAL2 DEBE SER MENOR O IGUAL AL VAL 1... \n")
        Val2= int(input("Ingrese el Valor 2 nuevamente .....:"))

    Resul = (Val1 - Val2)
    MostrarDatos(); #llama a la funcion a mostrar datos

if (Opc == 3 ):
    Operaciones = ("Ud selecciono la operacion Multiplicar")
    Resul = (Val1 * Val2)
    MostrarDatos(); #llama a la funcion a mostrar datos

if (Opc == 4 ):
    Operaciones = ("Ud selecciono la operacion Dividir")
    Resul = (Val1 / Val2)
    MostrarDatos(); #llama a la funcion a mostrar datos

