Algoritmo ejercicio5GuiaEjerciciosPropuestos
	Definir anno Como Real;
	salarioMensual = 180000;
	Escribir "Ingrese años de trabajo";
	Leer anno;
	si anno < 1 Entonces
		Escribir "Su salario es: ", salarioMensual*0.05;
	Finsi	
	si anno >= 1 y anno<2 Entonces
		Escribir "Su salario es: ", salarioMensual*0.07;
	FinSi
	si anno >= 2 y anno<5 Entonces
		Escribir "Su salario es: ", salarioMensual*0.1;
	FinSi
	si anno >= 5 y anno<10 Entonces
		Escribir "Su salario es: ", salarioMensual*0.15;
	FinSi
	si anno >= 10 Entonces
		Escribir "Su salario es: ", salarioMensual*0.20;
	FinSi
FinAlgoritmo
