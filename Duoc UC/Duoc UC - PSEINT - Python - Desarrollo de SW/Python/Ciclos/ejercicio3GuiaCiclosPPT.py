# Ingrese un número entero mayor a cero por teclado e 
# indique si es o no “Primo”.

cont = 0
while True:
    n = int(input("Ingrese un numero para saber si es primo o no: "))
    if n > 0:
        for x in range(2, n):
            if n % x != 0:
                cont += 1
            else:
                break
    print(f"Cantidad de primos entre 1 y {x+1}: {cont}")