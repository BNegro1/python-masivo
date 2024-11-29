import matplotlib.pyplot as plt

# Definir las preguntas y las respuestas
preguntas = [
    "Anxious mood",
    "Tension",
    "Fears",
    "Insomnia",
    "Intellectual",
    "Depressed mood",
    "Somatic (muscular)",
    "Somatic (sensory)",
    "Cardiovascular symptoms",
    "Respiratory symptoms",
    "Gastrointestinal symptoms",
    "Genitourinary symptoms",
    "Autonomic symptoms",
    "Behavior at interview"
]

respuestas = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] # Respuesta de severo

# Calcular la puntuación total
puntuacion_total = sum(respuestas) # En base a la función (sum)

# Calcular el promedio de las respuestas en la escala 0-4
promedio = sum(respuestas) / len(respuestas) 

# Escala para la interpretación del promedio
escala_interpretacion = [
    "No presente",
    "Leve",
    "Moderado",
    "Severo",
    "Muy severo"
] 

# Crear un gráfico de barras de las respuestas
plt.figure(figsize=(10, 6))
plt.barh(preguntas, respuestas, color='skyblue')
plt.xlabel('Puntuación (0-4)') # Label X
plt.title('Puntuación de HAM-A por Pregunta') # Titulo grafico
plt.xlim(0, 4)
plt.xticks(range(5))
plt.gca().invert_yaxis()

# Mostrar la puntuación total en el gráfico
plt.text(puntuacion_total + 0.1, len(preguntas) - 0.5, f'Total: {puntuacion_total}', fontsize=12)

# Mostrar el promedio en la escala 0-4
plt.text(4.2, -1, f'Promedio: {promedio:.2f}', fontsize=12)

# Mostrar la interpretación del promedio
interpretacion_promedio = escala_interpretacion[int(promedio)]
plt.text(4.2, -2, f'Interpretación: {interpretacion_promedio}', fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
