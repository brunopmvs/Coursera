"""
Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteirose devolve um número inteiro correspondente ao maior valor presente na lista recebida.
lista = [63,64,53,46,62,53,68,46,47,53,59,62,64, 78,45,50,48,58,45,52,45, 79, 512,60,54,46,54,62,65,5,7,61,5,1,66,64,6,6,58,52,46-45,-61,64,49,45,51,-5,58,59,46,53,50,55,65,53,-6,2,56]

print(maior_elemento(lista))


"""

def maior_elemento(lista):
    aux = lista[0]
    for x in lista:        
        if (aux < x):
            aux = x
        
    return aux







