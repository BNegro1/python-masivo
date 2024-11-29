from os import system
system ("cls")

print ("")
print ("EJERCICIO 3 GUIA 2 ")
print ("===================")
print ("")

print ("CALCULO DE NOTEBOOK")
print ("")

#VARIABLES

Producto= ""; 
Cantidad=  0; 
ValorUni=  0; 
Total=     0; 
Dcto=      0; 
Dcto20E=   0; 
DctoT10=   0; 
Dcto20=    0; 
Dcto10=    0; 
Interes=   0; 
Int=       0; 
DctoT=     0; 

#INGRESO DE DATOS
Producto= input("Ingrese producto........:"     )
Cantidad= int(input("Ingrese cantidad........:"))
ValorUni= int(input("Ingrese Valor...........:"))
Pago =    input("Ingrese forma de pago...:"     )

#CALCULO TOTAL
Total = (Cantidad * ValorUni)
Dcto10=  (Total * 10)  /100
Dcto20=  (Total * 20)  /100
DctoT10= (Total * 10)  /100
Dcto20E= (Total * 20)  /100
Interes= (Total * 10)  /100

print ("Monto total a pagar.....:", Total)
print ("")

if (Pago ==  "Efectivo"    or Pago == "efectivo" or Pago == "EFECTIVO"):
    print ("El pago seleccionado es.:", Pago); 
    DctoT= "Aplica 20%"
    Total= Total= (Total - Dcto20E)

    if (Total >1 and Total <= 700000 ):
        Dcto= "No aplica descuento"

    elif (Total >700000 and Total <=800000):
        Dcto= "Aplica descuento 10%"
        Total= (Total - Dcto10)

    else: 
        (Total >800000 and Total <=999999)
        Dcto= "Aplica descuento 20%"
        Total= (Total - Dcto20)

if (Pago ==  "Debito"    or Pago == "debito" or Pago == "DEBITO"):
    print ("El pago seleccionado es.:", Pago); 
    DctoT= "Aplica 10%"
    Total= (Total - DctoT10)

    if (Total >1 and Total <= 700000 ):
        Dcto= "No aplica descuento"

    elif (Total >700000 and Total <=800000):
        Dcto= "Aplica descuento 10%"
        Total= (Total - Dcto10)

    else: 
        (Total >800000 and Total <=999999)
        Dcto= "Aplica descuento 20%"
        Total= (Total - Dcto20)

if (Pago ==  "Credito"    or Pago == "credito" or Pago == "CREDITO"):
    print ("El pago seleccionado es.:", Pago); 
    Int= "Aplica interes del 10%"
    Total= (Total + Interes)

    if (Total >1 and Total <= 700000 ):
        Dcto= "No aplica descuento"

    elif (Total >700000 and Total <=800000):
        Dcto= "Aplica descuento 10%"
        Total= (Total - Dcto10)

    else: 
        (Total >800000 and Total <=999999)
        Dcto= "Aplica descuento 20%"
        Total= (Total - Dcto20)

print (""); 
print ("=============================================================="); 
print ("..............MUESTREO DE DATOS..............."); 
print ("=============================================================="); 
print ("Descuento Aplicado....................:",  Dcto); 
print ("Descuento Aplicado por forma de pago..:", DctoT); 
print ("Interes agregado......................:",   Int); 
print ("Monto total a pagar...................:", Total); 
print ("=============================================================="); 
print (""); 