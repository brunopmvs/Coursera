"""
Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
O programa deve receber os parâmetros a a a, b b b, e c c c da equação ax2+bx+c ax^2 + bx + c ax2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:
Quando não houver raízes reais imprima:
esta equação não possui raízes reais
Quando houver apenas uma raiz real imprima:
a raiz desta equação é X
onde X é o valor da raiz
Quando houver duas raízes reais imprima:
as raízes da equação são X e Y
onde X e Y são os valor das raízes.
Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente. Exemplos:
as raízes da equação são 1.0 e 2.0
as raízes da equação são -2.0 e 0.0

"""

import math

numA = int(input("Informe o valor de a: "))
numB = int(input("Informe o valor de b: "))
numC = int(input("Informe o valor de c: "))

delta = math.pow(numB, 2) - (4 * (numA * numC))
if (delta < 0):
    print("esta equação não possui raízes reais")

elif(delta == 0 ):
    x1 = ((-1*numB) + math.sqrt(delta)) / (2 * numA)
    print("a raiz desta equação é", x1)
elif (delta > 0 ):
    x1 = ((-1*numB) + math.sqrt(delta)) / (2 * numA)
    x2 = ((-1*numB) - math.sqrt(delta)) / (2 * numA)
    if(x1 > x2):
        temp = x1
        x1 = x2
        x2 = temp
    
    print("as raízes da equação são", x1, "e", x2)
