import numpy as np

def matriz_aleatoria(m:int, n:int):
    matriz = np.random.randint(-9,10, size=(m,n))
    return matriz

e = 0.001

A = np.array([[1, 1+e],
              [1-e, 1]])

A_inv = np.linalg.inv(A)

b = matriz_aleatoria(2,1)
print(b)

x = b @ A_inv
print(x)

