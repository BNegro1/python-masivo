from os import system;
system("cls"); \

#MENU de opciones 
print (""); 
print (" .... MENU DE OPCIONES ..... "); 
print ("============================="); 
print (" 1.- Operaciones Matematicas "); 
print (" 2.- Factura................."); 
print (" 3.- Promedio................");  
print (" 4.- Sueldo.................."); 
print (" 5.- Autor Programa..........."); 
print (""); 

Opcion= int(input("Ingrese Opcion(1-5) :")); 
print ("");

if (Opcion == 1):
    print ("")
    print ("Operaciones matematicas")
    print ("=======================")
    print (" 1. Sumar 2 valores")
    print (" 2. Sumar 3 valores")
    Operacion= int(input("Ingrese Opcion(1-3) :")) 
    print ("")
    #OPERACION SUMATIVA 1
    if (Opcion == 1):
        Suma1 = "Selecciono una suma de 2 valores"
        Val1 = "Ingrese un valor:"
        Val2 = "Ingrese un Valor:"
        Resultado = (Val1 + Val2); 
        print ("")
        print ("MUESTRA DE DATOS")
        print ("================")
        print ("")
        print("Ud. realizo una suma:......", Suma1); 
        print("El Valor ingresado:........:", Val1); 
        print("El Valor ingresado:........:", Val2); 
        print("El resultado es:.......", Resultado); 
        print("  "); 
    #OPERACION SUMA 2
    else: (Operacion == 2)
    Suma2 = "Selecciono una suma de 3 valores"
    Val1 = int(input("Ingrese un valor: ")); 
    Val2 = int(input("Ingrese un valor: ")); 
    Val3 = int(input("Ingrese un valor: ")); 
    Resultado = (Val1 + Val2 + Val3)
    print ("")
    print ("MUESTRA DE DATOS")
    print ("================")
    print ("Ud realizo una suma:", Suma2)
    print ("El valor ingresado:..", Val1)
    print ("El valor ingresado:..", Val2)
    print ("El valor ingresado:..", Val3)
    print ("El resultado es:", Resultado)
    print ("")
#OPERACION 2 FACTURAR
if (Operacion == 2):
    print(""); 
    print("Ud. ha selecccionado Factura"); 
    print("============================"); 
    Prod = input("Ingrese el producto................................:"); 
    Cant = int(input("Ingrese cantidad de producto .................:")); 
    Valor = int(input("Ingrese el valor del producto................:"));

    #FORMULA PARA DCTO
    Dcto = (Cant * Valor) 
    DctoA = ""
    Total = (Dcto)

    #MUESTRA DE DATOS
    print(""); 
    print("MUESTRA DE DATOS"); 
    print("================"); 
    print("Usted compro................:", Prod); 
    print("La Cantidad es..............:", Cant); 
    print("El precio del producto es..:", Valor); 
    print("El Descuento es.................:", );  
    print("El Total es.................:",Total); 
    print(""); 

 #OPERACION CALCULO DE PROMEDIO
if (Operacion == 3 ):
    print(""); 
    print("CALCULO DE PROMEDIO"); 
    print("================== "); 
    Rutt = input("Ingrese Rut del estudiante .............:"); 
    Nomm = input("Ingrese nombre del estudiante...........:"); 
    Asig = input("Ingrese su asignatura...................:"); 
    N1 = int(input("Ingrese nota 1 ......................:")); 
    N2 = int(input("Ingrese nota 2 ......................:")); 
    N3 = int(input("Ingrese nota 3 ......................:")); 
    N4 = int(input("Ingrese nota 4 ......................:")); 

    Prom = ( N1 + N2 + N3 + N4) /4; 
    if( Prom >= 10 and Prom <40 ):
        Situacion = "RIPLEY"; 

    if( Prom >= 40 and Prom <50 ):
        Situacion = "Aprobado"; 

    if( Prom >= 50 and Prom <=70 ):
        Situacion = "Eximido"; 

    print(""); 
    print("MUESTRA DE DATOS"); 
    print("================="); 
    print("Ingreso de rut............................................:", Rutt); 
    print("Ingrese su nombre.........................................:", Nomm); 
    print("Ingrese su asignatura.....................................:", Asig); 
    print("La Nota 1 es................................................:", N1); 
    print("La Nota 2 es................................................:", N2); 
    print("La Nota 3 es................................................:", N3); 
    print("La Nota 3 es................................................:", N4); 
    print("Su Promedio es............................................:", Prom); 
    print("La situacion del estudiante es.......................:", Situacion); 

#CALCULO DE SUELDO
if(Operacion == 4 ):
    print("CALCULO DE SUELDO"); 
    print("================="); 
    Nom = input("Ingrese su nombre......................................:"); 
    SueldoBase =int(input("Ingrese su sueldo base......................:")); 
    Bono = int(input("Ingrese bono.....................................:")); 
    Aguinaldo = int(input("Ingrese aguinaldo................................:")); 
    Anti = int(input("Ingrese anticipo.................................:")); 

    Sueldoliquido = (SueldoBase + Bono ) - (Anti)

    print("")
    print("MUESTRA DE DATOS"); 
    print(" ============== ");  
    print("El Nombre Del Trabajador...................:", Nom ); 
    print("El Sueldo Base Ingresado es..........:", SueldoBase); 
    print("El Anticipio Del Trabajador...............:", Anti ); 
    print("El Bono Del Trabajador es.................:", Bono );  
    print("El Sueldo Liquido Ingresado es...:", Sueldoliquido ); 
    print(""); 

if(Operacion == 5 ):
    print("Made by Andres, all rights reserved © 2022")