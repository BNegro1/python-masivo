Proceso numeroMagico
	Definir num, digito, suma, multiplicacion Como Real;
	Escribir "Ingrese un n�mero:";
	Leer num;

	suma <- 0; // Suma desde cero
	multiplicacion <- 1; // multiplicacion desde 1 (0 invalida)

	Mientras num > 0 Hacer
		digito <- num % 10; // "%" para obtener el ultimo digito del numero.
		suma <- suma + digito;
		multiplicacion <- multiplicacion * digito;
		num <- trunc(num / 10); // Trunca el valor de num
		
		Si num = 0 Entonces
			num = -1; // Sale del ciclo si num es cero
		FinSi
	FinMientras

	Si suma = multiplicacion Entonces
		Escribir "El n�mero es m�gico.";
	Sino
		Escribir "El n�mero no es m�gico.";
	FinSi
FinAlgoritmo
