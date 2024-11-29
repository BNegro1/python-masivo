Proceso promedioAsistencia
	Definir promedio, asistencia Como Real;
	// Promedio >= 4.0
	// Asistencia > 75% = 0.75
	Escribir "Ingrese promedio: ";
	Leer promedio;
	Escribir "Ingrese asistencia: ";
	Leer asistencia;
	Si promedio >= 4.0 y asistencia >= 75 Entonces
		Escribir "El alumno aprobó la asignatura.";
	SiNo
		Escribir "El alumno NO aprobó la asignatura.";
	FinSi
FinProceso
