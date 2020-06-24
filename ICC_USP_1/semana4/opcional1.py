"""
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
Digite um número inteiro: 13
primo
"""

num = int(input("Digite um número inteiro:"))
divisor = num
primo = True

while (divisor > 2):
    divisor = divisor - 1
    if num % divisor == 0:
        primo = False
        break
    else:
        primo = True       



print("primo") if primo else print("não primo")

multiplica (a, b):
    return a * b

print(multiplica(4,5))