Proceso ejercicio2SumaImparesEntre1y100
		Definir i, suma_impares Como Real;
		suma_impares = 0;
		para i = 1 Hasta 100 Hacer
			Si i % 2 <> 0 Entonces
				suma_impares = suma_impares + i;
			FinSi
		FinPara
		Escribir "Suma de impares entre 1 y 100: ", suma_impares;
FinProceso
