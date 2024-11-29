Proceso notasPromedio
	Definir n1, n2, n3, i Como Real;
	Definir confirmar Como Caracter;
	n1 = 0;
	n2 = 0;
	n3 = 0;
	Escribir "Ingrese nota 1 (entre 1,0 y 7,0)";
	Leer n1;
	Si n1 >= 1.0 y n1 <= 7.0 Entonces
		Escribir "Ingrese nota 2 (entre 1,0 y 7,0)";
		Leer n2;
		Si n2 >= 1.0 y n2 <= 7.0 Entonces
			Escribir "Ingrese nota 3 (entre 1,0 y 7,0)";
			Leer n3;
			Si n3 >= 1.0 y n3 <= 7.0  Entonces
				Escribir "Promedio: ", n1+n2+n3/3;
			SiNo
				Escribir "Ingrese la nota 3 correctamente.";
				Repetir
					Escribir "Ingrese nota 3: ";
					Leer n3;
				Hasta Que n3 >= 1.0 y n3 <= 7.0
			FinSi
		SiNo
			Escribir "Ingrese la nota 2 correctamente.";
			Repetir
				Escribir "Ingrese nota 2: ";
				Leer n2;
			Hasta Que n2 >= 1.0 y n2 <= 7.0
		FinSi
	SiNo
		Escribir "Ingrese la nota 1 correctamente.";
		Repetir
			Escribir "Ingrese nota 1: ";
			Leer n1;
		Hasta Que n1 >= 1.0 y n1 <= 7.0
	FinSi
	
FinAlgoritmo
