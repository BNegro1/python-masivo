favor = 0
contra = 0
conNoRetiro = 0
persona = 0
retiro0 = 0
ali = 0
montoMayor = 0 
while True:
    p1 = input("¿Está usted a favor de este tercer retiro?: ")
    if p1.upper() == "SI":
        favor += 1
        p2 = input("Ante la posibilidad de quedar en cero ¿realizaría de todas formas este retiro?: ")
        if p2.upper() == "SI":
            retiro0 += 1
            p3 = input("¿Qué haría con el dinero a retirar?: ")
            if p3.upper() == "ALIMENTOS":
                ali += 1
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break
            elif p3.upper() == "DEUDAS":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "INVERSION":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
        elif p2.upper() == "NO":
            conNoRetiro += 1
            p3 = input("¿Qué haría con el dinero a retirar?: ")
            if p3.upper() == "ALIMENTOS":
                ali += 1
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "DEUDAS":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "INVERSION":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            else:
                print("Ingrese un valor válido.")
        else:
            print("Ingrese un valor válido.")            
    elif p1.upper() == "NO":
        contra += 1
        p2 = input("Ante la posibilidad de quedar en cero ¿realizaría de todas formas este retiro?: ")
        retiro0 += 1
        if p2.upper() == "SI":
            retiro0 += 1
            p3 = input("¿Qué haría con el dinero a retirar?: ")
            if p3.upper() == "ALIMENTOS":
                ali += 1
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "Deudas":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "INVERSION":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
        elif p2.upper() == "NO":
            p3 = input("¿Qué haría con el dinero a retirar?: ")
            if p3.upper() == "ALIMENTOS":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            elif p3.upper() == "DEUDAS":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break               
            elif p3.upper() == "INVERSION":
                afp = int(input("Monto que tienen acumulado en la AFP: "))
                persona += 1
                if afp > 0:
                    montoMayor = afp                    
                    break                
            else:
                print("Ingrese un valor válido.")
        else:
            print("Ingrese un valor válido.")
    else:
        print("Ingrese un valor válido.")
        
# Calculos
prom = persona*0.01
if ali > 0:
    porcentaje = (retiro0/ali)*0.01

# Resultados

print("Resultados")

print(f"Promedio de personas: {prom}")
if ali > 0:
    print(f"Porcentaje de retiro: {porcentaje}")
print("Monto mayor AFP: $", montoMayor)