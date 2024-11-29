Proceso menu
	
	Definir op, f, i, j, coef, anio Como Real;
	Definir nom Como Caracter;
	Repetir
		Escribir "1.- Mostrar impares ";
		Escribir "2.- Mostrar largo del nombre";
		Escribir "3.- Calcular edad.";
		Escribir "4.- SALIR";
		Escribir "Ingrese una opcion: ";
		leer op;
		si op == 1 Entonces;
			Escribir "Ingrese numero inicio: ";
			Leer i;
			Escribir "Ingrese numero final: ";
			Leer f;
			para j = 1 Hasta f Hacer
				si j%2=0 Entonces
					Escribir j," Es par.";
				SiNo
					Escribir j," Es impar.";
				FinSi
			FinPara
		Sino Si op == 2 Entonces;
			Escribir "Ingrese nombre: ";
			Leer nom;
			Escribir "Su nombre tiene una longitud de ", Longitud(nom), " caracteres.";
		SiNo Si op == 3 Entonces;
			Escribir "Ingrese año de nacimiento: ";
			leer anio;
			Escribir "Usted tiene ", 2023-anio, " años.";
		SiNo Si op == 4 Entonces;
			Escribir "Gracias por su utilización.";
		SiNo;
			Escribir "Ingrese una opción valida.";
		FinSi
		FinSi
		FinSi
		FinSi

	Hasta Que op == 4	
FinProceso