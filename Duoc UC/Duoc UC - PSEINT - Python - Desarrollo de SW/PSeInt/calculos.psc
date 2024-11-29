Proceso calculos
	Definir num1, num2, suma, resta, multiplicacion, division Como real;
	Escribir  "Ingrese numero 1: ";
	Leer num1;
	Si num1 >= 1 Entonces
		Escribir "Ingrese numero 2: ";
		Leer num2; 
	SiNo
		Escribir "Ingrese un número mayor o igual a 1.";
		Si num2 >= 1 Entonces
			suma <- num1 + num2;
			resta <- num1 - num2;
			multiplicacion <- num1 * num2;
			division <- num1 / num2;
		FinSi
	FinSi
	Escribir "La suma es: ",suma;
	Escribir "La resta es: ",resta;
	Escribir "La multiplicacion es: ",multiplicacion;
	Escribir "La division es: ",division;
	
FinProceso
