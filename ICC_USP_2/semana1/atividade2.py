""""
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz
que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False
"""

def soma_matrizes(m1, m2):

    i_m1 = len(m1)
    j_m1 = len(m1[0])
    i_m2 = len(m2)
    j_m2 = len(m2[0])
    somaMatriz =[]

    if ((i_m1 == i_m1) and (j_m1 == j_m2)):
        for i in range(i_m1):
            linha1 = m1[i]
            linha2 = m2[i]
            somaLinha = []
            for j in range(j_m1):
                somaLinha.append(linha1[j] + linha2[j])
            somaMatriz.append(somaLinha)

        return somaMatriz

    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))
#[[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2) )