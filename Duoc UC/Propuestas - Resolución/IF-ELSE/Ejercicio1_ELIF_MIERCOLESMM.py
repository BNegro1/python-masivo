#EJERCICIO 1 IF - ELIF 11/05/22

from os import system 
system("cls")

#Se inicializa las variables ContR

print ("")
ContR = 0
ContA = 0
ContV = 0
ColorR =""; 
ColorV =""; 
ColorA =""; 
print ("")

Color = input ("Ingrese color.................................:")

if (Color == "Rojo" or Color == "ROJO" or Color == "rojo"):
    ContR = (ContR+1); 
    ColorR= "Rojo"; 
    print ("Ud. ha seleccionado el color",Color,"y tambien ingreso el color:.",Color); 
    print ("La cantidad de colores ingresados es:............................",ContR); 

elif (Color == "Verde" or Color == "VERDE" or Color == "verde"):
    ContV = (ContV+1); 
    ColorV= "Verde"; 
    print ("Ud. ha seleccionado el color",Color,"y tambien ingreso el color:.",Color); 
    print ("La cantidad de colores ingresados es:............................",ContV); 

elif (Color == "Azul" or Color == "AZUL" or Color == "azul"):
    ContA = (ContA+1); 
    ColorA= "Azul"; 
    print ("Ud. ha seleccionado el color",Color,"y tambien ingreso el color:.",Color); 
    print ("La cantidad de colores ingresados es:............................",ContA); 

else:
    print ("")
    print ("========================================")
    print ("El color seleccionado no esta disponible")
    print ("========================================")
    print ("")


print ("")
print ("...............MUESTRA DE DATOS FINALES................")
print ("=======================================================")
print ("El color ingresado por el usuario es..............:",Color)
print ("La cantidad de colores",ColorR,"ingresa fue.......:",ContR)
print ("La cantidad de colores",ColorV,"ingresa fue.......:",ContV)
print ("La cantidad de colores",ColorA,"ingresa fue.......:",ContA)
print ("=======================================================")
print ("")