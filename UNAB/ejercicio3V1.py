import numpy as np # Importamos la librería NumPy para trabajar con arrays
import matplotlib.pyplot as plt # Importamos la librería Matplotlib para hacer gráficos

# Definimos la función f(t)
def f(t):
    return 2 - 2*np.exp(-t/3)*np.cos(2*t)

# Creamos un array con los valores del eje x (t)
t = np.linspace(0, 20, 1000)

# Creamos un array con los valores correspondientes de f(t)
y = f(t)

# Creamos el gráfico y lo configuramos
plt.plot(t, y) # Graficamos los puntos (t, f(t))
plt.title('Gráfico de f(t)') # Añadimos un título al gráfico
plt.xlabel('t') # Añadimos una etiqueta para el eje x
plt.ylabel('f(t)') # Añadimos una etiqueta para el eje y

# Mostramos el gráfico
plt.show()
