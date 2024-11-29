estatura = float(input("Ingrese estatura: "))
peso = float(input("Ingrese peso: "))
edad = int(input("Ingrese edad de la persona: "))

imc = peso/estatura**2

if imc < 22.0 and edad < 45:
    print(f"IMC: {imc} | Edad {edad} | Bajo")
elif imc < 22.0 and edad >= 45:
    print(f"IMC: {imc} | Edad {edad} | Medio")
elif imc >= 22.0 and edad < 45:
    print(f"IMC: {imc} | Edad {edad} | Medio")
elif imc >= 22.0 and edad >= 45:
    print(f"IMC: {imc} | Edad {edad} | Alto")


    