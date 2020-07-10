"""
Exercício 2: Ordenação com selection sort
Implemente a função ordena(lista), que recebe uma lista com números inteiros 
como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o 
algoritmo selection sort.
"""



def ordena(lista):

    tamanhoLista = len(lista)

    for i in range (0, tamanhoLista):
        for j in range (i+1, tamanhoLista):
            if ( lista[i] > lista[j] ):
                lista[i], lista[j] = lista[j], lista[i]

    return lista

