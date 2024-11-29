Proceso numerosParesImparesInput
    Definir num1, num2, pares, impares, suma_impares Como Entero;
    pares = 0;
    impares = 0;
    suma_impares = 0;
    Escribir "Ingrese primer numero: ";
    Leer num1;
    Escribir "Ingrese segundo numero: ";
    Leer num2;
    Para i = num1 Hasta num2 Hacer
        Si i % 2 = 0 Entonces
            pares = pares + 1;
        Sino
            impares = impares + 1;
            suma_impares = suma_impares + i;
        FinSi
    FinPara
    Escribir "Cantidad de numeros pares entre ", num1, " y ", num2, ": ", pares;
    Escribir "Suma de los numeros impares entre ", num1, " y ", num2, ": ", suma_impares;
FinProceso
