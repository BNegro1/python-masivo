# Ejercicio N°1 Ciclo For 
# Ciclo repetitivo for ( for = para)

from os import system
system("cls")

print("");
print("...Ejemplo Repetir con ciclo For 1...");
print("=====================================");
print("");

# Ejemplo N°1 con tres argumentos, Inicia en 1, repite 5 veces el proceso de 1 en 1

for i in range(1, 6, 1):
    print(i, end=", ")  #prints: 1, 2, 3, 4, 5
    #print(i);

print("");
print("");

# Ejemplo N°2 con tres argumentos, Inicia en 1, repite 3 veces el proceso de 1 en 1
for i in range(1, 4):
    print(i, end=", ") #print: 1, 2, 3
    #print(i);

print("");
print("");


# Ejemplo N°3 con tres argumentos, Inicia en 0, repite 7 veces el proceso 
for i in range(7):
    print(i, end=", ") #print: 0, 1, 2, 3, 4, 5, 6, 7


print("");
print("");