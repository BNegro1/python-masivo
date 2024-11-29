Proceso numeroPrimo
	Definir n Como Entero;
	Definir divi Como Entero;
	Definir i como Entero;
	Escribir "Ingrese rango para calcular si es primo o no: ";
	leer n;
	divi = 0;
	Para i<-1 hasta n Con Paso 1 Hacer
		Si n % i == 0 Entonces
			divi = divi + 1;
		FinSi
	FinPara
	si divi == 2 Entonces
		Escribir "El numero es primo";
	SiNo
		Escribir "El numero no es primo";
		
	FinSi
FinProceso
