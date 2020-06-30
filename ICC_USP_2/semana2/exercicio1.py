"""
Sejam as matrizes A = (aij)mxn e B = (bjk)nxp

A . B = matriz D = (dik)mxp

donde,

dik = ai1 . b1k + ai2 . b2k + ... + ain . bnk
"""


def multiplicaMatriz(matrix1, matrix2):
    import numpy as np
    m1 = np.array(matrix1)
    i_m1 = len(matrix1)
    j_m1 = len(matrix1[0])
    m2 = np.array(matrix2)
    i_m2 = len(matrix2)
    j_m2 = len(matrix2[0])
    #matrixResult = np.zeros(shape=(i_m1,j_m2))
    matrixResult = []
    for i in range(i_m1):
        linha = []
        for j in range(j_m2):
            linha.append(0)
        matrixResult.append(linha)



    for i in range(i_m1):
        for j in range(j_m2):
            for k in range(j_m1):
                matrixResult[i][j] += matrix1[i][k]*matrix2[k][j]
    
    for i in matrixResult:
        print(i)


    

matriz1 = [[1, 2, 3], [ 4, 5, 6]]
matriz2 = [[1,2] , [3,4],[5,6]]
multiplicaMatriz(matriz1, matriz2)
    