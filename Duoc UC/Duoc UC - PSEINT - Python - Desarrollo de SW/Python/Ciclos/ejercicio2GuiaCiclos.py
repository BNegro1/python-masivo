while True:
    print(''' 
        1.- Mostrar impares
        2.- Mostrar largo del nombre
        3.- Calcular edad
        4.- SALIR
        
        ''')
    op = int(input("Ingrese una opción: "))
    if op == 1:
        n1 = int(input("Ingrese rango inicial: "))
        n2 = int(input("Ingrese rango final: "))
        for x in range(n1, n2):
            if x % 2 != 0:
                print(f'Numero impar: {x}')
    elif op == 2:
        nom = input("Ingrese nombre: ")
        print(f'El largo del nombre {nom} es:', len(nom))
    elif op == 3:
        e1 = int(input("Ingrese año de nacimiento: "))
        if e1 > 1930:
            print(f'Edad actual:', 2023-e1)
        else:
            print("Ingrese un año valido.")
    elif op == 4:
        print("Hasta luego.")
        break
    else:
        print("Ingrese una opción VALIDA.")
