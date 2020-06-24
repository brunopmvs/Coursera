"""
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

Exemplo: 
>>>lista = [2, 4, 2, 2, 3, 3, 1]
>>>remove_repetidos(lista)
[1, 2, 3, 4]
>>>remove_repetidos([1, 2, 3, 3, 3, 4])
[1, 2, 3, 4]

lista = [63,64,53,46,62,53,68,46,47,53,59,62,45,50,48,58,45,52,45,60,54,46,54,62,65,5,7,61,5,1,66,64,6,6,58,52,46-45,-61,64,49,45,51,-5,58,59,46,53,50,55,65,53,-6,2,56]
print(remove_repetidos(lista))
"""


def remove_repetidos(lista):
    i = 0
    tamanhoLista = len(lista)
    lista.sort()
    while( i < tamanhoLista):

        a = lista[i]
        if(a == lista[i-1]):
            del lista[i]
            tamanhoLista=len(lista)
            i = 0
        i += 1
    return(lista)



