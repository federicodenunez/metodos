# Crear función de suma y resta de vectores en R3 sin numpy :c
# Ejercicio 1

def suma_vectores_r3 (vector_a, vector_b):
    vr = []
    vr.append(vector_a[0] + vector_b[0])
    vr.append(vector_a[1] + vector_b[1])
    vr.append(vector_a[2] + vector_b[2])
    return vr

def suma_vectores (vector_a, vector_b):
    vr = []
    for i in range(len(vector_a)):
        vr.append(vector_a[i] + vector_b[i])
    return vr

def resta_vectores_r3 (vector_a, vector_b):
    vr = []
    vr.append(vector_a[0] - vector_b[0])
    vr.append(vector_a[1] - vector_b[1])
    vr.append(vector_a[2] - vector_b[2])
    return vr

def resta_vectores (vector_a, vector_b):
    vr = []
    for i in range(len(vector_a)):
        vr.append(vector_a [i] - vector_b[i])
    return vr

def escalar_vector (vector, x):
    vr = []
    for i in vector:
        vr.append(x*i)
    return vr

def multiplicar_vectores (vector_a, vector_b):
    vr = 0
    for i in range(len(vector_a)):
        vr = vr + (vector_a[i] * vector_b[i])
    return vr

vector_A = [1,2,3]
vector_B = [4,5,6]

vector_C = suma_vectores_r3(vector_A, vector_B)
vector_C = suma_vectores(vector_A, vector_B)

vector_D = resta_vectores_r3(vector_A, vector_B)
vector_D = resta_vectores(vector_A, vector_B)

vector_E = escalar_vector(vector_A, 2)
vector_F = multiplicar_vectores(vector_A, vector_B)

# Ejercicio 2
def suma_matrices_r3(matriz_A, matriz_B):
    """
    Sumo lista de matrices
    """
    vr = []
    vr.append(suma_vectores_r3(matriz_A[0], matriz_B[0]))
    vr.append(suma_vectores_r3(matriz_A[1], matriz_B[1]))
    vr.append(suma_vectores_r3(matriz_A[2], matriz_B[2]))
    return vr

def suma_matrices(matriz_A, matriz_B):
    """
    Sumo lista de matrices
    """
    vr = []
    for i in range(len(matriz_A)):
        vr.append(suma_vectores(matriz_A[i], matriz_B[i]))
    return vr

def resta_matrices_r3(matriz_A, matriz_B):
    """
    resta lista de matrices
    """
    vr = []
    vr.append(resta_vectores_r3(matriz_A[0], matriz_B[0]))
    vr.append(resta_vectores_r3(matriz_A[1], matriz_B[1]))
    vr.append(resta_vectores_r3(matriz_A[2], matriz_B[2]))
    return vr

def resta_matrices(matriz_A, matriz_B):
    """
    resta lista de matrices
    """
    vr = []
    for i in range(len(matriz_A)):
        vr.append(resta_vectores(matriz_A[i], matriz_B[i]))
    return vr

matriz_A = [[1,1,1], 
            [0,0,0],
            [-1,0,1]]
matriz_B = [[0,0,0], 
            [2,2,2],
            [1,0,-1]]
"""
print(suma_matrices_r3(matriz_A, matriz_B))
print(suma_matrices(matriz_A, matriz_B))
print(resta_matrices_r3(matriz_A, matriz_B))
print(resta_matrices(matriz_A, matriz_B))
"""

def escalar_matriz(matriz_A, x):
    vr = []
    for i in range(len(matriz_A)):
        vr.append(escalar_vector(matriz_A[i], x))
    return vr

#A = [[1, 2, 3], [4, 5, 6]]
#print(escalar_matriz(A,2))

def matriz_x_vector (matriz, vector):
    if (len(matriz[0]) == len(vector)):
        vr = []
        for i in range(len(matriz)):
            vr.append(multiplicar_vectores(matriz[i],vector))
        return vr
    else:
        return [[]]

"""
A = [[1, 2, 3], [4, 5, 6]]
V = [7,8,9]
print(matriz_x_vector(A,V))
"""

"""
def matriz_x_matriz (matriz_A, matriz_B):
    vr = []
    if (len(matriz_A[0]) == len(matriz_B)): # Si el numero de columnas es igual al numero de filas.
        for i in range(len(matriz_B)):
            #fila i = matriz_B[i]
            aux = []
            for j in range(len(matriz_A)):
            #columna i = matriz_A[j][i]
                aux.append(matriz_A[j][i])
            print(aux)
            vr.append(multiplicar_vectores(matriz_B,aux))
        return vr
    else:
        return [[]]
"""
def transponer_matriz(matrix):
    # Obtener el número de filas y columnas de la matriz
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Crear una nueva matriz transpuesta
    transposed_matrix = []
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        transposed_matrix.append(new_row)

    return transposed_matrix

def matriz_x_matriz (matriz_A, matriz_B): # O(n^2) ups
    vr = []
    new_B = transponer_matriz(matriz_B)
    if (len(matriz_A[0]) == len(new_B)): # Si el numero de columnas es igual al numero de filas.
        for i in range(len(matriz_A)): # transformar maariz y hacer tuqui por tuqui
            aux = []
            for j in range(len(new_B)):
                aux.append(multiplicar_vectores(matriz_A[i], new_B[j]))
            vr.append(aux)
        return vr
    else: 
        return [[]]

"""
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matriz_x_matriz(A,B))
"""