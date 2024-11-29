#EJERCICIO 2 CICLO FOR 
#ciclo repetitivo for (for = para)

#Realice un programa para 3 alumnos
#Datos a dde cada alumno: Rut, Nombre, Asignatura y promedio

from os import system
system ("cls")

#Inicializcion de las variables que ocupara el programa 
Rutt="" #Variable que almacenara el rut
Nomb="" #Variable que almacenara el nombre
Asig="" #Variable que almacenara la asignatura
Prom=0  #Variable que almacenara el promedio

for h in range(1, 4, 1):
    print("");
    print("...INGRESO DE DATOS CICLO FOR N°",h,"...");
    print("================================");
    Rutt= input("Ingrese el rut del alumno........:")
    Nomb= input("Ingrese el nombre del alumno.....:")
    Asig= input("Ingrese la asignatura del alumno.:")
    Prom= input("Ingrese el promedio del alumno...:")

    print("");
    print("............MUESTRA DE DATOS............");
    print("El rut del alumno es.......:", Rutt);
    print("El nombre del alumno es....:", Nomb);
    print("La asignatura del alumno es:", Asig);
    print("El promedio del alumno es..:", Prom);
    print("=======================================");
    print("=======================================");
    print("");

print("");
print("Ahora estoy fuera del ciclo For");
print("\n\n");
print("");

