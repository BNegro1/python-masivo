Proceso sujetoCredito
	Definir dicom Como Caracter;
	Definir sujeto Como Caracter;
	Definir sueldo Como Real;
	// Diseña un algoritmo que determine si una persona es sujeta de credito.
	// Para poder SER sujeto de credito no debe tener DICOM y debe ganar mas de $500.000 pesos
	Escribir "Tiene DICOM: ";
	Leer dicom;
	Si dicom = "N" Entonces
		Escribir "Ingrese sueldo: ";
		Leer sueldo;
		Si sueldo > 500000 Entonces
			Escribir "Usted está sujeto(a) a credito.";
		SiNo
			Escribir "Usted no está sujeto";
		FinSi
	SiNo
		Escribir "Usted es sujeto(a) de credito.";
	FinSi
	
FinProceso
