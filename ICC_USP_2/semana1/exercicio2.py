"""Escreva uma função que recebe um array de strings e devolve o menor em ordem lexicográfica, ignorando-se maiusculas e minúsculas
menor_string(meuStrig)

testa_menor("Ana", "maria", "João")
"""

def menor_string(lista):
    
    listaLimpa = []
    for x in lista:
        listaLimpa.append(x.strip().lower())
    

    menor = listaLimpa[0]

    for x in listaLimpa:
        if ( menor > x ):
            menor = x

    return menor

def teste(lista, esperado):
    resultado = menor_string(lista)

    if (resultado == esperado):
        print("Teste OK")
    else:
        print("Incorreto")



print (menor_string(["   Paulo ", " Miguel  ", "   Sophia " , "Arthur     ", " Helena", "Bernardo   ", "Valentina       ", 
"Heitor", " Laura ","Davi   ", "Isabella ", "Lorenzo ","Alice", "Manuela", "Théo", "Júlia", "Pedro","Ana", "maria", "João"]))