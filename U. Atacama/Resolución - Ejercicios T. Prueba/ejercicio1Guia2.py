cod_l = []
mes_l = []
año_l = []
pie_l = []
superficie_l = []
precio_l = []
año_l = []
propiedadMayor = 0
habitacionUnidad = 0
mejor_comision = 0
mejor_codigo = ""
numinmobiliaria = int(input("Ingrese cantidad de inmobiliarias a vender: "))
for i in range(numinmobiliaria):
    cod = int(input(f"Ingrese codigo {i+1}: "))
    cod_l.append(cod)
    mes = int(input(f"Ingrese mes (1-12) {i+1}: "))
    if mes >= 1 and mes <= 12:
        mes_l.append(mes)
    else:
        print("Ingrese un mes correcto.")
    año = int(input("Ingrese año: "))
    año_l.append(año)
    piezas = int(input(f"Ingrese habitaciones {i+1}: "))
    pie_l.append(piezas)
    superficie = int(input(f"Ingrese superficie en metros cuadrados {i+1}: "))
    superficie_l.append(superficie)
    precio = int(input(f"Ingrese precio {i+1}: "))
    precio_l.append(precio)
# Calculo de comision, codigo y año
for n in mes_l, cod_l:
    if mes == 10 and año == 2021:
        comision = 0.02
        if mes <= (año - 1) % 12 + 1:
            comision += 0.01
        comision_total = precio * comision
        if comision_total > mejor_comision:
            mejor_comision = comision_total
            mejor_codigo = n
venta = input("¿Desea realizar la venta? (S/N):")
if venta.upper() == 'S':
    comision = 1.02
    for x in pie_l:
        if 3 in pie_l:
            propiedadMayor += 1
    for y in pie_l:
        if (1 in pie_l):
            precio_superficie = precio / superficie
    print("Porcentaje de propiedades con mas de 3 habitaciones: ", propiedadMayor*0.1)
    print("Promedio de la relación precio-superficie de las propiedades con una sola habitación: ", precio_superficie)
    print("La propiedad con mejor comisión para octubre de 2021 es:", mejor_codigo)
    print("La comisión de venta de la propiedad es:", mejor_comision)    
elif venta.upper() == 'N':
    print("Hasta luego.")


