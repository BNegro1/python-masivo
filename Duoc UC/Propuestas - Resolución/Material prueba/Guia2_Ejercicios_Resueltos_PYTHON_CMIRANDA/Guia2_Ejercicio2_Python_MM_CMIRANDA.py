
from os import system
system ("cls")

print ("")
print ("EJERCICIO 2 GUIA 2 ")
print ("===================")
print ("")

print ("CALCULO DE PRODUCTO")
print ("")

#VARIABLES
Rutt=            ""; 
Producto=        ""; 
Valor=        0; 
CantidadProducto= 0; 
Dcto=             0; 
Cont10=           0; 
Cont20=           0; 
Cont=             0; 
Total=            0;  

#INGRESO DE DATOS
Rutt= input("Ingrese rut del comprador..................:")
Producto= input("Ingrese producto...........................:")
Cantidad= int(input("Ingrese cantidad del producto..............:"))
Valor= int(input("Ingrese valor del producto.................:"))

#CALCULO TOTAL DE LA COMPRA
Total= (Cantidad * Valor)
Dcto10= (Total * 10) / 100
Dcto20= (Total * 20) / 100

if (Total >1 and Total <= 99999):
    Cont10= Cont10+1
    Dcto= "Aplica descuento del 10%"; 
    Total= (Total - Dcto10)

elif (Total >99999 and Total <= 200000):
    Cont20= Cont20+1
    Dcto= "Aplica descuento del 20%";
    Total= (Total - Dcto20)

else:
    (Total >200000 and Total <= 999999)
    Cont= Cont+1
    Dcto= "No aplica descuento"; 



print ("")
print ("==========================================")
print (".............MUESTREO DE DATOS............")
print ("==========================================")
print ("")

print ("Su rut es..........................:",       Rutt)
print ("Producto(s) seleccionado(s)........:",   Producto)
print ("La cantidad es.....................:",   Cantidad)
print ("El Valor del producto es...........:",      Valor)
print ("Aplica descuento de................:",       Dcto)
print ("El monto total a pagar del cliente.:",      Total)
print ("")
print ("Total ventas con 10%...............:",     Cont10)
print ("Total Ventas con 20%...............:",     Cont20)
print ("Total ventas sin Dcto..............:",       Cont)
print ("")