import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,20)
y1 = (-1/2)*1 + (3/2)*x
y2 = (-1/4)*1 + (3/2)*x

fig,ax = plt.subplots()
ax.plot(x, y2)
ax.plot(x, y1)

plt.show()

# Si 2*b1 = b2 entonces el sistema tendra solucion. Y seran infinitas, pues viendolo graficamente serian dos rectas
# iguales, (pues y2 es 2*y1). De ser distintos 2b1 y b2, el sistema no tendra solucion, graficamente serian 
# dos rectas paralelas. Al no intersecarse, no hay ningun x tal que se satisfacen las dos ecuaciones.

