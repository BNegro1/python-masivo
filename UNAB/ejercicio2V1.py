from ejercicio1V1 import ejecutarFunc # Importamos una función llamada "ejecutarFunc" desde un archivo llamado "ejercicio1V1"

class EstadisticasCurso: # Definimos una clase llamada "EstadisticasCurso"
    def __init__(self, nombre_archivo): # Definimos el método constructor de la clase, que recibe el nombre de un archivo como parámetro
        self.notas = [] # Creamos una lista vacía llamada "notas"
        with open(nombre_archivo, "r") as archivo: # Abrimos el archivo en modo lectura y lo asignamos a una variable llamada "archivo"
            for linea in archivo: # Iteramos sobre cada línea del archivo
                nombre, nota_str = linea.strip().split(": ") # Dividimos cada línea en dos partes: nombre y nota
                nota = float(nota_str) # Convertimos la nota (que está como una cadena de caracteres) a un número decimal
                self.notas.append(nota) # Añadimos la nota a la lista de notas

    def nota_maxima(self): # Definimos un método llamado "nota_maxima" que retorna la nota máxima del curso
        return max(self.notas)

    def nota_promedio(self): # Definimos un método llamado "nota_promedio" que retorna la nota promedio del curso
        return sum(self.notas) / len(self.notas)

    def nota_minima(self): # Definimos un método llamado "nota_minima" que retorna la nota mínima del curso
        return min(self.notas)

    def cantidad_aprobados(self): # Definimos un método llamado "cantidad_aprobados" que retorna la cantidad de estudiantes que aprobaron el curso
        return sum(nota >= 4.0 for nota in self.notas)

    def cantidad_reprobados(self): # Definimos un método llamado "cantidad_reprobados" que retorna la cantidad de estudiantes que reprobaron el curso
        return sum(nota < 4.0 for nota in self.notas)


if __name__ == "__main__": # Si este archivo es el programa principal que se está ejecutando...
    ejecutarFunc() # Llamamos a la función "ejecutarFunc" que importamos al principio (no se muestra el código de esa función)
    estadisticas_curso = EstadisticasCurso("notas.txt") # Creamos un objeto de la clase "EstadisticasCurso" con el nombre del archivo que contiene las notas
    print(f"Nota máxima del curso: {estadisticas_curso.nota_maxima()}") # Imprimimos la nota máxima del curso
    print(f"Nota promedio del curso: {estadisticas_curso.nota_promedio()}") # Imprimimos la nota promedio del curso
    print(f"Nota mínima del curso: {estadisticas_curso.nota_minima()}") # Imprimimos la nota mínima del curso
    print(f"Cantidad de estudiantes aprobados: {estadisticas_curso.cantidad_aprobados()}") # Imprimimos la cantidad de estudiantes que aprobaron el curso
    print(f"Cantidad de estudiantes reprobados: {estadisticas_curso.cantidad_reprobados()}") # Imprimimos la cantidad de estudiantes que reprobaron el curso
