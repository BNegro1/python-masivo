Algoritmo CalcularUtilidad
	Definir salario, antiguedad, utilidad Como Real;
	
	salario <- 180000;
	
	Escribir "Ingrese la antigüedad del trabajador en años:";
	Leer antiguedad;
	
	Si antiguedad < 1 Entonces
		utilidad <- salario * 0.05;
	Sino Si antiguedad >= 1 y antiguedad < 2 Entonces
		utilidad <- salario * 0.07;
	Sino Si antiguedad >= 2 y antiguedad < 5 Entonces
		utilidad <- salario * 0.10;
	Sino Si antiguedad >= 5 y antiguedad < 10 Entonces
		utilidad <- salario * 0.15;
	Sino
		utilidad <- salario * 0.20;
	FinSi
	FinSi
	FinSi
	FinSi
	Escribir "La utilidad del trabajador es:", utilidad;
	
FinAlgoritmo