# Escriba un programa que lea un número entero y muestre el número en cuenta regresiva hasta llegar a
# cero.

n = int(input("Ingrese numero: "))
n+=1
for x in range(1, n+1):
    n = n - 1
    print(n)