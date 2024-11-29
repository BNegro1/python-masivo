nom = input("Ingrese nombre del articulo: ")
clave = int(input("Ingrese clave del articulo: "))
precio = int(input("Ingrese precio original: "))
desc = int(input("Ingrese precio con descuento: "))

if clave == 01:
    print(f'Descuento de {nom} es de 10%', 0.9*precio)
elif clave == 02:
    print(f'Descuento de {nom} es de 20%', 0.8*precio)