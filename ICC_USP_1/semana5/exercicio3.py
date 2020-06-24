"""
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True

"""


def vogal (x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        return True
    else:
        return False  


