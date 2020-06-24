"""Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída."""

num = int(input("Digite o valor de n:"))
result = 1
while(num > 0):
    result = num * result
    num -=1

print(result)
