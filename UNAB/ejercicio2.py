import ejercicio1

estudiantes = ejercicio1.cargar_notas("notas.txt")

promedio = ejercicio1.obtener_promedio(estudiantes)
maxima = ejercicio1.obtener_maxima(estudiantes)
minima = ejercicio1.obtener_minima(estudiantes)
aprobados, reprobados = ejercicio1.obtener_aprobados_reprobados(estudiantes)

print("Promedio:", promedio)
print("Máxima:", maxima)
print("Mínima:", minima)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
