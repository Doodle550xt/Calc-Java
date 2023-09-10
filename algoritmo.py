import matplotlib.pyplot as plt
import numpy as np

# Creamos una lista de valores de x
x = np.linspace(0, 100 , 100)  # Generamos 100 puntos entre -10 y 10

# Calculamos los valores correspondientes de y
y = x**2
y1 = np.log(x)
y2 = x
y3 = x*(np.log(x))
y4 = [1]*100
y5 = 2**x

# Graficamos la función y añadimos etiquetas
plt.plot(x, y, label='y = x^2')
plt.plot(x, y1, label='y = log(x)')
plt.plot(x, y2, label='y = x')
plt.plot(x, y3, label='y = x*log(x)')
plt.plot(x, y4, label='y = 1')
plt.plot(x, y5, label='y = 2^x')

# Añadimos etiquetas y título
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfico de varias funciones')

# Establecemos los límites del eje Y
plt.ylim(0, 8000)

# Añadimos una leyenda
plt.legend()

# Mostramos el gráfico
plt.show()

