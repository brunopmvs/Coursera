"""
Exercício 3.2
Dados um número inteiro n, n > 0, e um dígito d. 0 <= d <= 9, determinar quantas vezes d ocorre em n.
"""
print("Este algoritmo dirá quantas vezes determinado número aparece em outro")

num = int(input("Informe um numero qualquer maior que 0: "))

numdivisor = int(input("Informe o numero buscado:"))

counter = 0

while (num > 1):
    if (num % 10 == numdivisor):
        counter +=1
        num = num // 10
    else:
        num = num // 10

print("O número %d aparece %d vezes no número informado." %(numdivisor, counter))

