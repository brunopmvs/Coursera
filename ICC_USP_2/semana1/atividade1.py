"""
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro
 e imprime as dimensões da matriz recebida, no formato iXj.

Exemplos:
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
3X1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
2X3
"""

# def dimensoes(matriz):
#     """Recebe uma matriz como parâmetro
#     e imprime as dimensões da matriz recebida, no formato iXj."""
#     i = len(matriz)
#     j = len(matriz[0])

#     dimensoes = str(i) + "X" + str(j)
#     return str(dimensoes)

# print(dimensoes([[1, 2], [3, 4]]))

def dimensoes(matriz):
    i = 0
    j = 0
    for x in matriz:
        i += 1
        j = 0
        for z in x:
            j += 1
    print(str(i) + "X" + (str(j)))