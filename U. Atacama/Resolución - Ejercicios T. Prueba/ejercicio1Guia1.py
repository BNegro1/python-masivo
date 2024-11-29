sb = 0
bono = 0
may = 0
nivel = input("Ingrese nivel educacional del trabajor: ")
region = input("Ingrese región del trabajador: ")
hijos = int(input("Ingrese cantidad de hijos: "))
if nivel.upper() == 'Profesional':
    sb = 500000
    bono = 20000*hijos
    t = sb + bono
    print("Resumen")
    print(f"Nivel: {nivel} \n Región: {region} \n Hijos: {hijos} \n Sueldo: {t} ")    
elif nivel.upper() == 'Tecnico' and hijos > 4:
    sb = 30000
    bono = 20000*hijos
    may = int(input("¿Cuántos son mayores de 18 años?: "))
    t = sb + bono
    print("Resumen")
    print(f"Nivel: {nivel} \n Región: {region} \n Hijos: {hijos} \n Sueldo: {t} ")    
elif region.upper() == 'Antofagasta':
    bono = 30000*hijos
    t = sb + bono
    print("Resumen")
    print(f"Nivel: {nivel} \n Región: {region} \n Hijos: {hijos} \n Sueldo: {t} ")    
elif region.upper() != 'Antofagasta':
    bono = 20000*hijos
    t = sb + bono
    print("Resumen")
    print(f"Nivel: {nivel} \n Región: {region} \n Hijos: {hijos} \n Sueldo: {t} ")
else:
    t = sb + bono
    print("Resumen")
    print(f"Nivel: {nivel} \n Región: {region} \n Hijos: {hijos} \n Sueldo: {t} ")

    