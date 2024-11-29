Proceso ejercicio5SumaCuadradosSeparados
    Definir i, num, suma_cuadrados Como Entero;
    suma_cuadrados = 0;
    Escribir "Ingrese un número menor a 500: ";
    Leer num;
    para i = 0 Hasta (num-4) con Paso 4 Hacer
        suma_cuadrados = suma_cuadrados + (i * i) + ((i + 4) * (i + 4));
    FinPara
    Escribir "La suma de los cuadrados de los números separados por 4 posiciones hasta ", num, " es: ", suma_cuadrados;
FinProceso
