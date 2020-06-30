"""
Como proposto na primeira vídeo-aula da semana, escreva uma função 
imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime
 a matriz, linha por linha. Note que NÃO se deve imprimir espaços após 
 o último elemento de cada linha!

Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral
 adiciona uma quebra de linha ao final, mas você pode controlar isso usando o 
 argumento opcional "end"dessa forma:

>>>print("oi")
oi
>>>
>>>print("oi", end="")
oi>>>

minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6
"""

def imprime_matriz(matriz):
    i_matriz = len(matriz)
    j_matriz = len(matriz[0])
    i = 0
    j = 0
    linha = ""

    while(i < i_matriz):
        j = 0
        linha = ""
        while(j < j_matriz):
            linha += str(matriz[i][j]) + " "
            j += 1
        i += 1
        print(linha.rstrip())
 


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)