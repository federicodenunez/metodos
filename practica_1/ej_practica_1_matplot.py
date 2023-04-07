import numpy as np
import matplotlib.pyplot as plt

def recta(x, m, b, c):
    return (m*x + c)/b

x = np.linspace(-100, 100, 100)
"""
y = recta(x, 1, 1, 0)
plt.plot(x, y, label = "linea 1")

y2 = recta(x, -3, 6, 18)
plt.plot(x, y2, label = "linea 2")
"""

# ecuacion: 3x - 2y = b1 <=> y = -3x + b1 / -2
#recta(x, multiplicador de x, multiplicador de y, b1)
#y3 = recta(x, -3, -2, 10)

fig, ax = plt.subplots(1,1, figsize = (10, 5)) # el 1,1 es para indicar que quiero un plot
#ax.plot(x, y3)
# esta bien

def sistema_2_ecuaciones_simples(x, f1:list, f2:list):
    y_aux_1 = recta(x, f1[0], f1[1], f1[2])
    y_aux_2 = recta(x, f2[0], f2[1], f2[2])
    ax.plot(x, y_aux_1)
    ax.plot(x, y_aux_2)
     
"""
b1:int = 1
b2:int = 1
funcion_1_ej_7 = [-3, -2, b1]
funcion_2_ej_7 = [-6, 4, b2]
sistema_2_ecuaciones_simples(x, funcion_1_ej_7, funcion_2_ej_7)
"""
print(x)
y_abs_neg = -x
y_abs_pos = x
x_neg = x[0:50]
x_pos = x[51,99]
print(x_neg)
ax.plot(x_neg, y_abs_neg)
ax.plot(x_pos, y_abs_pos)

plt.legend()
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title('Titulo')
plt.show()


