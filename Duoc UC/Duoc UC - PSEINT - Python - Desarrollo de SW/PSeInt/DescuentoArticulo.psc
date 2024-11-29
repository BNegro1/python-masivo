Algoritmo DescuentoArticulo
	Definir nombreArticulo Como Cadena;
	Definir clave Como Entero;
	Definir precioOriginal, precioConDescuento Como Real;
	
	Escribir "Ingrese el nombre del articulo: ";
	Leer nombreArticulo;
	
	Escribir "Ingrese la clave del articulo (01 o 02): ";
	Leer clave;
	
	Escribir "Ingrese el precio original del articulo: ";
	Leer precioOriginal;
	
	Si clave == 01 Entonces
		precioConDescuento <- precioOriginal * 0.9;
	SiNo Si clave == 02 Entonces;
		precioConDescuento <- precioOriginal * 0.8;
	
	Sino
		Escribir "Clave invalida";
		
		Escribir "Articulo: ", nombreArticulo;
		Escribir "Clave: ", clave;
		Escribir "Precio original: $", precioOriginal;
		Escribir "Precio con descuento: $", precioConDescuento;
	FinSi
	FinSi
FinAlgoritmo