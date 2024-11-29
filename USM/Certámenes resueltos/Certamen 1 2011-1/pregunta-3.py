#Primero, necesitamos saber cuantos valores van a ingresar.
cant = int(input("Cuantos valores ingresara? "))

#Algunas variables que usaremos
maximo = -float('inf')
minimo = float('inf')

#Ahora pedimos todos los valores:
for i in range(cant):
	valor = float(input("Valor "+str(i+1)+": "))
	if valor > maximo: maximo = valor
	if valor < minimo: minimo = valor

print ("El rango es "+str(maximo - minimo))