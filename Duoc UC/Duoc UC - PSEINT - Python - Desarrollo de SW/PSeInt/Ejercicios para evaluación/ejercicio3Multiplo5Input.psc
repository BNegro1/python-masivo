Proceso ejercicio3MultiploDesde5Input
	Definir i, multiplo, inputusuario, suma_multiplos Como Real;
	multiplo = 0;
	suma_multiplos = 0;
	Escribir "Ingrese numero: ";
	Leer inputusuario;
	para i = 1 Hasta inputusuario Hacer
		Si i % 5 = 0 Entonces // Si "Y % X == 0" es MULTIPLO sino, no lo es XD
			multiplo = multiplo + 1;
			suma_multiplos = suma_multiplos + i;
		FinSi
	FinPara
	Escribir "Multiplos de 5 entre 1 y ", inputusuario,": ", multiplo;
	Escribir "Suma de los multiplos: ", suma_multiplos;
FinProceso
