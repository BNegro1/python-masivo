# PROGRAMA DEMOSTRACION PYTHON

print (""); # Asigna una linea en blanco
print (" Calculo de sueldo");
print ("---------------------");
print (""); # Asigna una linea en blanco

Rutt= "30.568.789-9";
Nombre= "JPerez"; 
Cargo= "Supervisor";
SueldoBase= 400000;
Aguinaldo= 20000;
Anticipo= 30000;

print (""); 

#Calculo del bono 20% del sueldo base
Bono= (SueldoBase * 20)/ 100;

print (""); 

#Calculo del sueldo liquido
SueldoLiquido= (SueldoBase + Bono + Aguinaldo) - (Anticipo);

print (""); # Asigna una linea en blanco
print (" Muestra de datos del sueldo ");
print ("------------------------------");
print (""); # Asigna una linea en blanco
print ("El rut del trabajador es:..........................", Rutt);
print ("El nombre del trabajador es:.......................", Nombre);
print ("El Cargo del trabajador es:........................", Cargo);
print ("El Sueldo base del trabajador es:..................", SueldoBase);
print ("El Aguinaldo del trabajador es:....................", Aguinaldo);
print ("El Anticipo del trabajador es:.....................", Anticipo);
print ("El bono del trabajador es:.........................", Bono);
print ("El Sueldo liquido final del trabajador es:.........", SueldoLiquido);
print ("");
print ("");