estado = input("Usted suele estar dormido o sentado en reposo? (D/R): ")
mins = int(input("Ingrese cantidad de minutos: "))
if estado == 'D' or estado == 'd':
    d = 1.08
    print("Calorias consumidas estando dormido: ", d * mins)
elif estado == 'R' or estado == 'r':
    r = 1.08
    print("Calorias consumidas estando en reposo: ", r * mins)