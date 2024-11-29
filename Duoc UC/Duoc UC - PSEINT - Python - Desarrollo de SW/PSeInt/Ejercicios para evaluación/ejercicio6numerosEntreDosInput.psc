Proceso ejercicio6numerosEntreDosInput
    Definir num1, num2, contador, suma_multiplos Como Entero;
    contador = 0;
    suma_multiplos = 0;
    Escribir "Ingrese primer numero: ";
    Leer num1;
    Escribir "Ingrese segundo numero: ";
    Leer num2;
    Para i = num1 Hasta num2 Hacer
        Si i % 2 <> 0 Y i % 5 <> 0 Entonces
            Escribir i;
            contador = contador + 1;
			Sino Si i % 2 = 0 O i % 5 = 0 Entonces
					suma_multiplos = suma_multiplos + i;
			FinSi

        FinSi
    FinPara
    Escribir "Cantidad de numeros entre ", num1, " y ", num2, " (sin multiplos de 2 y 5): ", contador;
    Escribir "Suma de los multiplos de 2 y 5: ", suma_multiplos;
FinProceso
