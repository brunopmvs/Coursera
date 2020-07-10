"""
Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros como 
parâmetro e devolve o booleano True se a lista estiver ordenada e False se a lista 
não estiver ordenada.
"""

def ordenada(lista):
    ordem = True
    tamanhoLista = len(lista)
    i = 0
    while (i < tamanhoLista-1 ):
        if ( (lista[i] > lista[i+1])):
            ordem = False 
            return ordem
        else:
            ordem = True
        i += 1
    return ordem


