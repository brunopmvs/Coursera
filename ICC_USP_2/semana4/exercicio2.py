"""
Implemente a função busca(lista, elemento), que busca um determinado elemento em 
uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado não 
existir na lista, a função deve devolver o booleano False.

busca(['a', 'e', 'i'], 'e')
# deve devolver => 1

busca([12, 13, 14], 15)
# deve devolver => False
"""

def busca(lista, elemento):
    
    tamanhoLista = len(lista)
    for x in range (0, tamanhoLista):
        if (lista[x] == elemento):
            return x

    return False
