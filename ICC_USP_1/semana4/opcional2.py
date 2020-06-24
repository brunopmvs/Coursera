"""
Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 12345
não

Digite um número inteiro: 1011
sim
"""

num = int(input("Digite um número inteiro:"))
adjacente = False

while (num > 0):
    numParcial = num % 10 
    if(numParcial == ((num // 10) % 10) ):
        adjacente = True
        break

    num = num // 10
    
print("Sim") if adjacente else print("Não")