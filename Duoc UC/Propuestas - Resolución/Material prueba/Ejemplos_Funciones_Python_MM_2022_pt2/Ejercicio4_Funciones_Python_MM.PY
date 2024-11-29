#EJEMPLO 4 FUNCIONES
#Funcion con retorno de valores o retorno de parametros

from os import system
system ("cls")

print (""); 
print ("... EJEMPLO DE FUNCIONES CON RETORNO DE PARAMETROS...")
print ("")

#Definicion de la funcion OperaMate
def OperaMate1 (Val1a, Val2a):
    Result= (Val1a + Val2a); 
    return (Result); 

#Llamo a la funcion y le mando los argumentos 
print ("")
Num1a = int(input("Ingrese el Valor 1 a..:")); 
Num2a = int(input("Ingrese el Valor 2 a..:")); 
print (OperaMate1(Num1a,Num2a)); 

print ("======================================")

def OperaMate2(Val1b, Val2b):
    result= (Val1b + Val2b);
    print("el valor de la suma es:", result)

print ("")
Num1b = int(input("Ingrese valir 1B..:"))
Num2b = int(input("Ingrese valir 2B..:"))
OperaMate2(Num1b,Num2b)