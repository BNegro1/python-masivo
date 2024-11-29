Algoritmo ejercicio2GuiaEjerciciosPropuestos
	Definir n1, clave Como Caracter;
	Definir precioOri, precioDesc Como Real;
	precioDesc = 0
	precioOri = 10000
	n1 = "Polera";
	Escribir n1;
	Escribir n2;
	Escribir "Ingrese clave (01, 02): "
	Leer clave;
	Si clave = "01" Entonces
		precioDesc = 0.9;
		Escribir "Precio descuento: ", precioOri*precioDesc
	FinSi
	Si clave = "02" Entonces
		precioDesc = 0.80;
		Escribir "Precio descuento: ", precioOri*precioDesc
	FinSi
FinAlgoritmo
