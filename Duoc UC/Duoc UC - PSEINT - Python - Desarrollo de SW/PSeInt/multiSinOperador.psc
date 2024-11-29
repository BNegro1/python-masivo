Proceso multiSinOperadorConFor
	Definir numero1,numero2,i,multi,resultado Como Entero;
	Escribir 'Ingrese primer numero: ';
	Leer numero1;
	Escribir 'Ingrese segundo numero: ';
	Leer numero2;
	resultado = 0;
	Para i<-1 Hasta numero2 Con Paso 1 Hacer
		resultado = resultado+numero1; // Suma sucesiva de valores anteriores.
	FinPara
	Escribir 'Resultado es: ', resultado;
FinProceso
