# Ingresar por teclado 5 números enteros, luego debe indicar:
# Cuántos números son mayores a cero
# Cuántos números son menores a cero
# Cuántos números son iguales a cero

n_m = 0
n_men = 0
n_cer = 0
for x in range(5):
    n = int(input(f"Ingrese numero {x+1}: "))
    if n > 0:
        n_m += 1
    elif n < 0:
        n_men += 1
    elif n == 0:
        n_cer += 1
print(f"Numeros mayores a cero: {n_m} | Numeros menores a cero: {n_men} | Numeros iguales a 0: {n_cer}")