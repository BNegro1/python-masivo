# Ejemplo 2 FUNCIONES CON CHICLO WHILE
# EJEMPLO DE FUNCIONES SIN RETORNO DE VALORES O SIN RETORNO DE PARAMETROS

from os import system
system ("cls")

NombreC    = ""
NombreP    = ""
CantE      = 0
ValorE     = 0
TotalVenta = 0


print ("")
print ("EJEMPLO 2 DE FUNCIONES")
print ("======================")
print ("")

#Funcion CalculoVentaEntrada
def CalculoVentaEntrada():
    global TotalVenta
    TotalVenta= (ValorE * CantE); 

#Funcion MostrarDatosEntrada
def MostrarDatosEntrada(): 
    print ("")
    print ("........Muestra de datos en Funcion........")
    print ("===========================================")
    print ("El nombre del cliente es.............:", NombreC)
    print ("El nombre de la pelicula es..........:", NombreP)
    print ("El valor de la entrada es............:", ValorE)
    print ("la cantidad de entradas compradas es.:", CantE)
    print ("El total a pagar es..................:", TotalVenta)
    print ("===========================================")

#Programa Principal
i=1; 
while (i <= 3):
    print ("....Cliente N°",i,"....")
    print ("========================")
    NombreC= input("Ingrese nombre del cliente....:")
    NombreP= input("Ingrese nombre de la pelicula.:")
    ValorE = int(input("Ingrese valor de la entrada...:"))
    CantE  = int(input("Ingrese cantidad de entradas..:"))

    #Llama a la funcion CalculoVentasEntrada
    CalculoVentaEntrada(); 

    #LLama a la funcion MuestraDatosEntrada
    MostrarDatosEntrada(); 

    i +=1 #INCREMENTO DE 1 EN 1 ==> I = 1 + 1

print("")
print("FIN DEL PROGRAMA")
print("")