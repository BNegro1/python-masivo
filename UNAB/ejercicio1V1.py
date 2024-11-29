# Se define una clase llamada Curso
class Curso:
    # El constructor de la clase inicializa un diccionario vacío para guardar las notas
    def __init__(self):
        self.notas = {}

    # Método que permite registrar las notas de los estudiantes
    def registrar_notas(self):
        # El ciclo se ejecuta mientras la cantidad de elementos en el diccionario de notas sea menor a 30
        while len(self.notas) < 30:
            # Se pide al usuario ingresar el nombre del estudiante
            nombre = input("Ingrese el nombre del estudiante (Solo primer nombre / 'ok' o 'OK' para salir.): ")
            # Si el usuario ingresa 'ok' o 'OK', se rompe el ciclo y se sale del método
            if nombre == "OK" or nombre == 'ok':
                break
            # Si el nombre del estudiante ya existe en el diccionario, se informa al usuario y se vuelve a pedir el nombre
            if nombre in self.notas:
                print("Ya se ingresó un estudiante con ese nombre.")
                continue
            # Se pide al usuario ingresar la nota del estudiante
            nota = float(input("Ingrese la nota del estudiante (entre 1.0 y 7.0): "))
            # Si la nota está fuera del rango válido, se informa al usuario y se vuelve a pedir la nota
            if nota < 1.0 or nota > 7.0:
                print("La nota debe estar entre 1.0 y 7.0.")
                continue
            # Si el nombre y la nota son válidos, se agregan al diccionario de notas
            self.notas[nombre] = nota

    # Método que guarda las notas en un archivo de texto
    def guardar_notas(self, nombre_archivo):
        # Se abre el archivo de texto en modo escritura
        with open(nombre_archivo, "w") as archivo:
            # Se recorre el diccionario de notas y se escriben los nombres y notas en el archivo de texto
            for nombre, nota in self.notas.items():
                archivo.write(f"{nombre}: {nota}\n")

# Función que ejecuta el código principal
def ejecutarFunc():
    # Se crea una instancia de la clase Curso
    curso = Curso()
    # Se llama al método registrar_notas() para que el usuario ingrese las notas de los estudiantes
    curso.registrar_notas()
    # Se llama al método guardar_notas() para que las notas se guarden en un archivo de texto llamado "notas.txt"
    curso.guardar_notas("notas.txt")
