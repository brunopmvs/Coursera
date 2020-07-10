"""
Exercício 1: Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.
"""

def lista_grande(n):
    import random
    lista = []
    inicio = int(random.random() * -1 * 1000)
    fim = int(random.random() * 1000)
    for x in range(n):
        a = int(random.randint(inicio, fim))
        lista.append(a)

    
    return lista
