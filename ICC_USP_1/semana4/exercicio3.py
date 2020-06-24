"""Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
Digite um número inteiro: 123
6
"""

num = int(input("Digite um número inteiro:"))
result = 0

while (num > 0):
    result += num % 10
    num //= 10

print(result)


    