"""
Receba um número inteiro positivo na entrada e imprima os n n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
Digite o valor de n: 5
1
3
5
7
9
"""

num = int(input("Digite o valor de n:"))
i = 1
while(num > 0 ):
    print(i)
    num -=1
    i+=2
