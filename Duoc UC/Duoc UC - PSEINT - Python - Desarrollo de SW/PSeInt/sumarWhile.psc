Proceso sumarSinOperadorEnWhile
	Definir numero1,numero2,i,multi,resultado Como Entero;
	Escribir 'Ingrese primer numero: ';
	Leer numero1;
	Escribir 'Ingrese segundo numero: ';
	Leer numero2;
	resultado = 0;
	i = 1;
	Mientras i <= numero2 Hacer
		resultado = resultado+numero1; // Suma sucesiva de valores anteriores.
		i = i + 1;
	FinMientras
	Escribir 'Resultado es: ', resultado;
FinProceso
