# Ingrese un número entero mayor a cero por 
# teclado e indique si es o no “Perfecto”.
n = int(input("Ingrese un número entero mayor a cero: "))
suma = 0
if n <= 0:
    print("El número ingresado no es mayor que cero.")
else:
    for i in range(1, n):
        if n % i == 0: # Verifica que "i" sea divisor.
            suma += i # Se aumenta la suma.
    if suma == n: # Si la suma es igual al numero ingresado...
        print(f"El número {n} es perfecto.")
    else:
        print(f"El número {n} no es perfecto.")
