"""Exercício 1 - Primos

Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a 
quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

Exemplo:
>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30"

def n_primos(x):

    nprimos = 0
    n = 2
    while(n <= x):
        while(x % n == 0):
            nprimos += 1
            x /=n
        n +=1


    return nprimos 

num = int(input("Informe um número: "))
print(n_primos(num))
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

def n_primos(x):

    nprimos = 0
    n = 2
    while(n <= x):
        if(ePrimo(n)):
            nprimos+=1

        n +=1


    return nprimos 

num = int(input("Informe um número: "))
print(n_primos(num))
