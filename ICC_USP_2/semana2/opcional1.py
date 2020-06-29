"""
Exercício 1: Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro
 parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string.
  Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o 
numero de vogais presentes na frase. Quando ele for definido como "consoantes", 
a função deve devolver o número de consoantes presentes na frase. Se este parâmetro
 não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

Exemplos:

conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13
"""

# def conta_letras(frase, contar="vogais"):
    
#     cont = 0
#     string = frase.lower()
#     string = string.strip()
#     string = string.replace(" ", "")
#     tamanhoString = len(string)

#     for x in string:
#         if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
#             cont +=1

#     if (contar.lower() == "vogais"):
#         return cont

    
#     if  (contar.lower() == "consoantes"):
#         return tamanhoString - cont

def conta_letras(frase, contar="vogais"):
    
    atributo = contar.lower()

    vogais = 0
    consoantes = 0
    numeros = 0
    string = frase.lower()
    string = string.strip()
    string = string.replace(" ", "")

    if( atributo == "vogais"):

        for x in string:
            if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
                vogais +=1
        return vogais

    if (atributo == "consoantes"):
        for x in string:
            if (ord(x) >=97 and ord(x) <= 122):
                consoantes += 1
            if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
                consoantes -= 1
        return consoantes

    if (atributo == "números"):
        for x in string:
            if (ord(x) >=48 and ord(x) <= 57):
                numeros += 1
        return numeros

    




# print(conta_letras('programamos em python'))
# # deve devolver 6

# print(conta_letras('programamos em python', 'vogais'))
# # deve devolver 6

# print(conta_letras('programamos em python', 'consoantes'))
# # deve devolver 13

# print(conta_letras('programamos desde 1988 em python', 'números'))
# # deve devolver 13