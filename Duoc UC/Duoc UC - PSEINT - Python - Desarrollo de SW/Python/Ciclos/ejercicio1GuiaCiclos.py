cho = 0
ita = 0
veg = 0
t = 0

while True:
    print(''' 
        1) Realizar Venta
        2) Cerrar Turno
        3) Salir
          
          ''')
    op = int(input("Ingrese una opción: "))
    if op == 1:
        while True:
            print('''
                        1.- DuocChoripan $1200
                        2.- DuocItaliano $1500
                        3.- DuocVegano $2000
                        4.- Salir
                  ''')
            op2 = int(input("Ingrese una opción: "))
            if op2 == 1:
                cho += cho + 1
                t = cho * 1200
            elif op2 == 2:
                ita += ita + 1
                t = t + (ita*1500)
            elif op2 == 3:
                veg += veg + 1
                t = t + (veg*2000)
            elif op2 == 4:
                break
    elif op == 2:
        print("Total a pagar: ",t )
    elif op == 3:
        break
    else:
        print("Ingrese una opción valida.}")