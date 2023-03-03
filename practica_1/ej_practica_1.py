# Crear función de suma y resta de vectores en R3 sin numpy :c

def suma_vectores_r3 (vector_a, vector_b):
    vr = []
    vr.append(vector_a[0] + vector_b[0])
    vr.append(vector_a[1] + vector_b[1])
    vr.append(vector_a[2] + vector_b[2])
    return vr

def resta_vectores_r3 (vector_a, vector_b):
    vr = []
    vr.append(vector_a[0] - vector_b[0])
    vr.append(vector_a[1] - vector_b[1])
    vr.append(vector_a[2] - vector_b[2])
    return vr

vector_A = [1,2,3]
vector_B = [1,1,1]

vector_C = suma_vectores_r3(vector_A, vector_B)
vector_D = resta_vectores_r3(vector_A, vector_B)


def suma_matrices_r3(matriz_A, matriz_B):
    """
    Sumo lista de matrices
    """
    vr = []
    vr.append(suma_vectores_r3(matriz_A[0], matriz_B[0]))
    vr.append(suma_vectores_r3(matriz_A[1], matriz_B[1]))
    vr.append(suma_vectores_r3(matriz_A[2], matriz_B[2]))
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

matriz_A = [[1,1,1], 
            [0,0,0],
            [-1,0,1]]
matriz_B = [[0,0,0], 
            [2,2,2],
            [1,0,-1]]

print(suma_matrices_r3(matriz_A, matriz_B))
print(resta_matrices_r3(matriz_A, matriz_B))

