# Abrimos el archivo y leemos todas las líneas
with open("medicamentos.txt") as archivo:
    lineas = archivo.readlines()

# Creamos dos diccionarios para almacenar la información
farmacias = {}
medicamentos = {}

# Recorremos las líneas del archivo y agregamos la información a los diccionarios
for linea in lineas:
    datos = linea.strip().split(",")
    if datos[0].startswith("F"):
        farmacias[datos[0]] = int(datos[1])
    else:
        medicamentos[datos[0]] = int(datos[1])

# 1. Farmacia con más medicamentos
farmacia_max = max(farmacias, key=farmacias.get)
print("Farmacia con más medicamentos:", farmacia_max)

# 2. Farmacia con menos medicamentos
farmacia_min = min(farmacias, key=farmacias.get)
print("Farmacia con menos medicamentos:", farmacia_min)

# 3. Farmacias que venden "RAMIPRIL"
farmacias_ramipril = [farmacia for farmacia, cantidad in medicamentos.items() if farmacia == "RAMIPRIL"]
print("Farmacias que venden RAMIPRIL:", ", ".join(farmacias_ramipril))

# 4. Stock total de "PARACETAMOL" entre todas las farmacias
stock_paracetamol = sum([cantidad for medicamento, cantidad in medicamentos.items() if medicamento == "PARACETAMOL"])
print("Stock total de PARACETAMOL:", stock_paracetamol)

# 5. Stock total de medicamentos entre todas las farmacias y total de farmacias
total_medicamentos = sum(medicamentos.values())
total_farmacias = len(farmacias)
print("Stock total de medicamentos:", total_medicamentos)
print("Total de farmacias:", total_farmacias)
