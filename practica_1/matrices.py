def suma_vectorial(v1:list, v2:list) -> list:
    vr:list = []
    i:int = 0
    while i < len(v1):
        vr.append(v1[i] + v2[i])
        i += 1
    return vr

def resta_vectorial(v1:list, v2:list) -> list:
    vr:list = []
    i:int = 0
    while i < len(v1):
        vr.append(v1[i] - v2[i])
        i += 1
    return vr

def multiplicacion_vectorial(v1:list, v2:list) -> int:
    vr:int = 0
    i:int = 0
    while i < len(v1):
        vr += v1[i] * v2[i]
        i += 1
    return vr

def suma_matricial(m1:list[list], m2:list[list]) -> list[list]:
    n = len(m1[0])
    i = 0
    vr = []
    while i < n:
        aux = []
        j = 0
        while j < n:
            aux.append(m1[i][j]+m2[i][j])
            j+=1
        vr.append(aux)
        i+=1
    return vr

def resta_matricial(m1:list[list], m2:list[list]) -> list[list]:
    n = len(m1[0])
    i = 0
    vr = []
    while i < n:
        aux = []
        j = 0
        while j < n:
            aux.append(m1[i][j]-m2[i][j])
            j+=1
        vr.append(aux)
        i+=1
    return vr

def vector_por_escalar(v:list, e:int) -> list:
    vr = []
    for elem in v:
        vr.append(elem*e)
    return vr

def matriz_por_escalar(m:list[list], e) -> list[list]:
    vr = []
    for elem in m:
        aux = []
        for x in elem:
            aux.append(x*e)
        vr.append(aux)
    return vr

def trasponer_matriz(x):
    vr = []
    i, j = 0, 0
    while j < len(x[0]):
        new_fila = []
        while i < len(x):
            new_fila.append(x[i][j])
            i = i + 1
        vr.append(new_fila)
        i = 0
        j = j + 1
    return vr

def matriz_por_matriz(mat1:list[list], mat2:list[list]) -> list[list]:
    n1 = len(mat1[0])
    m1 = len(mat1)
    m2 = len(mat2[0])
    vr = []
    mt2 = trasponer_matriz((mat2))
    fila=0
    columna=0
    while fila < n1:
        aux = []
        columna = 0
        while columna < m2:
            newnumber = 0
            i = 0
            while i < m1:
                newnumber += mat1[fila][i] * mt2[columna][i]
                i+=1
            aux.append(newnumber)
            columna += 1
        vr.append(aux)
        fila+=1
    return vr

def matriz_por_vector(m:list[list],v:list) -> list[list]:
    aux = []
    for number in v:
        aux.append([number])
    return matriz_por_matriz(m, aux)

# Ej 3

'''
a = [-8, 9]
b = [3, -1]
c = [2, -4]

print(resta_vectorial(suma_vectorial(vector_por_escalar(a,2) , vector_por_escalar(b, 4)), c))
print(suma_vectorial(vector_por_escalar(a, 3), vector_por_escalar(suma_vectorial(vector_por_escalar(b, 2), c), 1/2)))
'''

# Ej 4

'''
a=[1,3,1] 
b=[5,-3,2]
c=[-3,-4,2]

print(multiplicacion_vectorial(a,b))
print(multiplicacion_vectorial(suma_vectorial(a, vector_por_escalar(b, 2)), resta_vectorial(c, b)))
print(multiplicacion_vectorial(a, b) - multiplicacion_vectorial(suma_vectorial(b,c), a) + multiplicacion_vectorial(vector_por_escalar(a, 2), c))
'''
