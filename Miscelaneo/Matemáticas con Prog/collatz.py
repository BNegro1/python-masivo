import numpy as np
import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Solicitar al usuario la cantidad de números para generar las secuencias
try:
    num_numeros = int(input("Introduce la cantidad de números para generar las secuencias: "))
    if num_numeros <= 0:
        raise ValueError()
except ValueError:
    print("Por favor, introduce un número entero positivo válido.")
    exit(1)

# Calcular las secuencias de Collatz y Fibonacci
collatz = collatz_sequence(num_numeros)
fibonacci = fibonacci_sequence(num_numeros)

# Asegurarse de que ambas secuencias tengan la misma longitud
min_length = min(len(collatz), len(fibonacci))
collatz = collatz[:min_length]
fibonacci = fibonacci[:min_length]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(range(1, min_length + 1), collatz, label='Collatz', marker='o', linestyle='-')
plt.plot(range(1, min_length + 1), fibonacci, label='Fibonacci', marker='x', linestyle='--')
plt.xlabel('Número')
plt.ylabel('Valor')
plt.title('Comparación de Secuencias de Collatz y Fibonacci')
plt.legend()
plt.grid(True)
plt.show()
