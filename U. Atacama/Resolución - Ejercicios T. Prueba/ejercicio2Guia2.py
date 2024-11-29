# Inicializar variables
total_operaciones = 0
suma_operaciones = 0
resta_operaciones = 0
multiplicacion_operaciones = 0
division_operaciones = 0

# Ciclo principal
while True:
    # Pedir operación al usuario
    operacion = input("Ingrese la operación (+, -, x, /): ")
    
    # Salir si el usuario ingresa "salir"
    if operacion == "salir":
        break
    
    # Verificar que la operación sea válida
    if operacion not in ["+", "-", "x", "/"]:
        print("Operación no válida")
        continue
    
    # Pedir números al usuario
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    
    # Verificar que los números sean enteros
    if not num1.isdigit() or not num2.isdigit():
        print("Debe ingresar números enteros")
        continue
    
    # Convertir números a enteros
    num1 = int(num1)
    num2 = int(num2)
    
    # Realizar la operación correspondiente
    if operacion == "+":
        resultado = num1 + num2
        suma_operaciones += 1
    elif operacion == "-":
        resultado = num1 - num2
        resta_operaciones += 1
    elif operacion == "x":
        resultado = num1 * num2
        multiplicacion_operaciones += 1
    elif operacion == "/":
        if num2 == 0:
            print("No se puede dividir por cero")
            continue
        resultado = num1 / num2
        division_operaciones += 1
    
    # Incrementar el contador de operaciones totales
    total_operaciones += 1
    
    # Mostrar resultado temporal
    print(f"Resultado: {resultado}")
    
    # Preguntar al usuario si desea ver el resultado final o agregar otra operación
    opcion = input("¿Desea ver el resultado final? (s/n): ")
    
    # Mostrar resultado final si el usuario lo desea
    if opcion == "s":
        print(f"Resultado final: {resultado}")
        break

# Calcular el porcentaje de operaciones de tipo suma
porcentaje_suma = suma_operaciones / total_operaciones * 100

# Determinar el tipo de operación más realizada
tipo_operacion = max(suma_operaciones, resta_operaciones, multiplicacion_operaciones, division_operaciones)
if tipo_operacion == suma_operaciones:
    tipo_operacion = "+"
elif tipo_operacion == resta_operaciones:
    tipo_operacion = "-"
elif tipo_operacion == multiplicacion_operaciones:
    tipo_operacion = "x"
elif tipo_operacion == division_operaciones:
    tipo_operacion = "/"

# Mostrar resultados finales
print(f"Cantidad de operaciones totales: {total_operaciones}")
print(f"Tipo de operación mas realizada: {tipo_operacion}")
