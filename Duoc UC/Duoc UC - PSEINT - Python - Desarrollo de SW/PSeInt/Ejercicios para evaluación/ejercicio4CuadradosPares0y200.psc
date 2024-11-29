Proceso ejercicio4CuadradosPares0y200
	Definir i, suma_cuadrados como real;
	suma_cuadrados = 0;
	para i = 0 Hasta 200 Hacer
		Si i % 2 = 0 Entonces
			suma_cuadrados = suma_cuadrados + i*i;
		FinSi
	FinPara
	Escribir "Suma de los cuadrados par: ", suma_cuadrados;
FinProceso
