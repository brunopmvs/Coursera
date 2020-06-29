"""
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que 
recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem 
lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

Exemplos:
primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
"""

def primeiro_lex(lista):
    
    listaLimpa = []
    for x in lista:
        listaLimpa.append(x.strip())
    

    menor = listaLimpa[0]

    for x in listaLimpa:
        if ( menor > x ):
            menor = x

    return menor

# print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# print(primeiro_lex(['AAAAAA', 'b']))