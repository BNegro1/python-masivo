Proceso fibonacci
    Definir n, i, val_1, val_2, nuevo_val como Entero;
    Escribir "Ingrese termino N para generar sucesi�n de fibonacci:";
    Leer n;
    Si n < 2 Entonces
        Escribir "El n�mero de t�rminos debe ser mayor o igual a 2.";
    Sino
        Escribir "La sucesi�n de Fibonacci es:";
        val_1 <- 0;
        val_2 <- 1;
        Escribir val_1;
        Escribir val_2;
        Para i <- 3 Hasta n Con Paso 1 Hacer
            nuevo_val <- val_1 + val_2;
			val_1 <- val_2;
            val_2 <- nuevo_val;
            Escribir nuevo_val;
        FinPara
    FinSi
FinProceso
