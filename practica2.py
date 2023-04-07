import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 5

def crear_matriz_ceros():
    matriz = np.zeros((4, 5))
    return matriz

def crear_matriz_unos():
    matriz = np.ones((5,3))
    return matriz

def matriz_identidad(n:int):
    matriz = np.identity(n)
    return matriz

def matriz_diagonal_peculiar(lista):
    matriz = matriz_identidad(len(lista))
    for i in range(len(lista)):
        matriz[i] = matriz[i] * lista[i]
    return matriz

# matriz_a_5 = crear_matriz_ceros()
# print(matriz_a_5)
# matriz_b_5 = crear_matriz_unos()
# print(matriz_b_5)
# matriz_c_5 = matriz_identidad(5)
# print(matriz_c_5)
# matriz_d_5 = matriz_diagonal_peculiar([3,4,2,5])
# print(matriz_d_5)

# Ejercicio 6

def matriz_aleatoria(m:int, n:int):
    matriz = np.random.randint(-9,10, size=(m,n))
    return matriz

#print(matriz_aleatoria(6,4))

# Ejercicio 7
A = matriz_aleatoria(4,4)
#A = [[ 6, -7,  1,  7],
#     [ 4, -5,  6,  1],
#     [-2,  0 , 5,  4],
#     [ 0,  2,  0 ,-6]]

I4 = matriz_identidad(4)

matriz_resultado = ((A+I4)*(A-I4))
matriz_resultado_2 = (A**2)-I4
def iguales(A, B):
    return A == B
    
#print(iguales(((A+I4)*(A-I4)), ((A**2)-I4))) # me sirve

A_1 = matriz_aleatoria(4,4)
A_2 = matriz_aleatoria(4,4)
A_3 = matriz_aleatoria(4,4)
B_1 = matriz_aleatoria(4,4)
B_2 = matriz_aleatoria(4,4)
B_3 = matriz_aleatoria(4,4)

# print(iguales(((A_1+B_1)*(A_1-B_1)), (A_1**2) - (B_1**2)))
# print(iguales(((A_2+B_2)*(A_2-B_2)), (A_2**2) - (B_2**2)))
# print(iguales(((A_3+B_3)*(A_3-B_3)), (A_3**2) - (B_3**2)))

# Sí, son todas iguales
# Conclusión... las matrices cuadradas funcionan como una variable (incognita x normal)

# Ejercicio 10

def detectar_patron_sombreado(M:np.matrix):
        condicion = True
        while condicion == True:
            x = np.random.randint(2, size=(4,1))
            x_transpuesta = x.transpose()
            resultado = x_transpuesta @ M @ x

            if resultado == 0:
                print("Encontre un patron para M: ")
                print(x)
                condicion = False            

M = np.array([[1, 0, -1, 0],
              [0, 1, 0, 0],
              [-1, 0, 1, 0],
              [0, 0, 0, 1]])

M2 = np.array([[1, 0, 0, -1],
                   [0, 1, 0, -1],
                   [0, 0, 1, 0],
                   [-1, -1, 0, 2]])

#detectar_patron_sombreado(M) # 0 0 0 0 y 1 0 1 0
#detectar_patron_sombreado(M2) # 0 0 0 0 y 1 1 0 1

#Repasar teoria de esto





