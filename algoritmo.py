import matplotlib.pyplot as plt
import numpy as np

# Creamos una lista de valores de x
x = np.linspace(0, 100 , 100)  # Generamos 100 puntos entre -10 y 10

# Calculamos los valores correspondientes de y
y = x**2
y1 = np.log(x)
y2 = x
y3 = x*(np.log(x))
y4 = x**2

# Graficamos la función
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

# Añadimos etiquetas y título
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfico de y = x^2')

# Mostramos el gráfico
plt.show()
