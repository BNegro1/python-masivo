class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre}: {self.nota}"


def crear_estudiante():
    while True:
        nombre = input("Ingrese el nombre del estudiante ('ok' / 'OK' para salir): ")
        if nombre.upper() == "OK":
            return None
        nota = float(input("Ingrese la nota del estudiante (entre 1.0 y 7.0): "))
        if nota < 1.0 or nota > 7.0:
            print("La nota debe estar entre 1.0 y 7.0. Intente de nuevo.")
            continue
        return Estudiante(nombre, nota)


def cargar_notas(nombre_archivo):
    estudiantes = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, nota = linea.strip().split(": ")
            estudiantes.append(Estudiante(nombre, float(nota)))
    return estudiantes


def obtener_promedio(estudiantes):
    notas = [estudiante.nota for estudiante in estudiantes]
    return sum(notas) / len(notas)


def obtener_maxima(estudiantes):
    notas = [estudiante.nota for estudiante in estudiantes]
    return max(notas)


def obtener_minima(estudiantes):
    notas = [estudiante.nota for estudiante in estudiantes]
    return min(notas)


def obtener_aprobados_reprobados(estudiantes):
    aprobados = 0
    reprobados = 0
    for estudiante in estudiantes:
        if estudiante.nota >= 4.0:
            aprobados += 1
        else:
            reprobados += 1
    return aprobados, reprobados


estudiantes = []
for i in range(30):
    print(f"Ingrese los datos del estudiante {i + 1}:")
    estudiante = crear_estudiante()
    if estudiante is not None:
        estudiantes.append(estudiante)
    else:
        break

with open("notas.txt", "w") as archivo:
    for estudiante in estudiantes:
        archivo.write(f"{estudiante}\n")