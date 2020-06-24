"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:
>>> maior_primo(100)
97
>>> maior_primo(7)
7
"""

def ePrimo(x):

    divisor = x
    primo = True

    while (divisor > 2):
        divisor -= 1
        if x % divisor == 0:
            primo = False
            break
        else:
            primo = True

    return primo    

def maior_primo(x):

    while(x > 0):
        
        if (ePrimo(x)):
            return x
        x -= 1

    else:
        return  None   
    
