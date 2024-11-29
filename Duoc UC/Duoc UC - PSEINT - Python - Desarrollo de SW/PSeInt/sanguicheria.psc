Proceso sanguicheria
	Definir op, f, i, j, cho, ita, veg, z, total Como Real;
	Definir nom Como Caracter;
	cho = 0;
	ita = 0;
	veg = 0;
	total = 0;
	Repetir
		Escribir "1.- Realizar venta.";
		Escribir "2.- Cerrar turno.";
		Escribir "3.- SALIR";
		Escribir "Ingrese una opcion: ";
		leer op;
		si op == 1 Entonces;
			cho = 0;
			ita = 0;
			veg = 0;
			total = 0;
			Mientras op <> 4 Hacer
				Escribir "1.- DuocChoripan: $1200.";
				Escribir "2.- DuocItaliano: $1500.";
				Escribir "3.- DuocVegano: $2000.";
				Escribir "4.- Salir.";
				leer op;
				Si op == 1 Entonces
					cho = cho + 1200;
					total = total + 1200;
				Sino Si op == 2 Entonces
					ita = ita + 1500;
					total = total + 1500;
				Sino Si op == 3 Entonces
					veg = veg + 2000;
					total = total + 2000;
				Sino si op == 4 Entonces
					FinSi
				FinSi
				FinSi
				FinSi
				Escribir "Total a pagar: $", total, ".";
			FinMientras
				
		
		Sino Si op == 2 Entonces;
				Escribir "Cerrar turno ";

				Escribir "Venta de Duoc Choripan: ", cho;
				Escribir "Venta de Duoc Italiano: ", ita;
				Escribir "Venta de Duoc Vegano: ", veg;
		SiNo Si op == 3 Entonces;
				Escribir "Ingrese año de nacimiento: ";
				leer anio;
				Escribir "Usted tiene ", 2023-anio, " años.";
		SiNo Si op == 4 Entonces;
		FinSi
		Finsi	
		FinSi
		Finsi	
	Hasta Que op == 4
		
FinProceso

