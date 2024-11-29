Proceso servicioMilitar
	
	// Define variables.
	Definir edad Como Entero; Definir sexo Como Caracter;
	
	//Impresión y lectura.
	Escribir "Ingrese edad: ";
	Leer edad;
	Escribir "Ingrese sexo (F o M): ";
	Leer sexo;
	
	// Sentencias de control.
	Si edad >= 18 y sexo == "M" o sexo == "m" Entonces
		Escribir "Usted puede hacer el servicio militar.";
	SiNo
		Escribir "Usted NO puede hacer el servicio miitar.";
	FinSi
FinProceso