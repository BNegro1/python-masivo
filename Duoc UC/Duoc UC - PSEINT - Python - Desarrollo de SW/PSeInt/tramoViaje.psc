Algoritmo tramoViaje
	Definir tiempo_total, duracion, horas, minutos Como Real;
	// Variable para el tiempo total de viaje
	tiempo_total = 0;
	
	// Comenzamos pidiendo una duraci�n de tramo
	Escribir "Duraci�n tramo: ";
	Leer duracion;
	
	// Mientras la duraci�n no sea cero...
	Mientras (duracion <> 0) Hacer
		// Sumamos la duraci�n a nuestro contador
		tiempo_total = tiempo_total + duracion;
		// Y pedimos la siguiente duraci�n
		Escribir "Duraci�n tramo: ";
		Leer duracion;
	FinMientras
	
	// Cuando la duraci�n ingresada sea cero, expresamos
	// el tiempo total en horas y minutos
	horas = tiempo_total / 60;
	minutos <- tiempo_total % 60;
	Escribir "Tiempo total del viaje: ", horas, ":", minutos, " horas";
FinAlgoritmo