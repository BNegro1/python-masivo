Algoritmo tramoViaje
	Definir tiempo_total, duracion, horas, minutos Como Real;
	// Variable para el tiempo total de viaje
	tiempo_total = 0;
	
	// Comenzamos pidiendo una duración de tramo
	Escribir "Duración tramo: ";
	Leer duracion;
	
	// Mientras la duración no sea cero...
	Mientras (duracion <> 0) Hacer
		// Sumamos la duración a nuestro contador
		tiempo_total = tiempo_total + duracion;
		// Y pedimos la siguiente duración
		Escribir "Duración tramo: ";
		Leer duracion;
	FinMientras
	
	// Cuando la duración ingresada sea cero, expresamos
	// el tiempo total en horas y minutos
	horas = tiempo_total / 60;
	minutos <- tiempo_total % 60;
	Escribir "Tiempo total del viaje: ", horas, ":", minutos, " horas";
FinAlgoritmo