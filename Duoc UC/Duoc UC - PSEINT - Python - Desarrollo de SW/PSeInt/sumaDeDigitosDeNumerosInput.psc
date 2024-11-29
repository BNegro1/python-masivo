Proceso sumaDeDigitosInput
	Definir suma, num, total, i, digito Como real;
	Escribir "Ingrese un numero: ";
	Leer num;
	suma = 0;
	i = 0;
	Mientras num <> 0 Hacer
		digito = trunc(num)%10;
		suma = suma + digito;
		num = trunc(num / 10);
		i = i + 1;
	FinMientras
	Escribir suma;
FinProceso
// Diseñar un algoritmo que indique si un numero es magico, condicion: la suma de sus digitos sea igual a la multiplicacion de sus digitos
// Validar un numero menor que 10