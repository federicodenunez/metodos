import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Grafico 1

x = np.linspace(-100,100)
y = 3*x + 5

fig,ax = plt.subplots()
ax.plot(x, y)
plt.show()

# Grafico 2

x = np.linspace(-100,100)
y = (1/25)*(x**2) - 2*x + 10

fig,ax = plt.subplots()
ax.plot(x, y)
plt.show()

# Grafico 3

x1 = np.linspace(-100,0)
x2 = np.linspace(0,100)
y1 = -10*x1 + 5
y2 = 10*x2 + 5

fig,ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
plt.show()

# Grafico 4

x = np.linspace(-100,100)
y = abs(x)

fig,ax = plt.subplots()
ax.plot(x, y)
plt.show()