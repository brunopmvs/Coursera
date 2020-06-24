"""
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima
crescente
se eles forem dados em ordem crescente. Caso contrário, imprima
não está em ordem crescente
"""

numA = int (input("Informe o primeiro numero: "))
numB = int (input("Informe o segundo numero: "))
numC = int (input("Informe o terceiro numero: "))

if (numA < numB and numB < numC):
    print("crescente")
else:
    print("não está em ordem crescente")