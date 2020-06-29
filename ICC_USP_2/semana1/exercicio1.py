"""Escrever uma função que recebe uma lista de String contendo 
nomes de pessoas como parametro e devolve o mais curto. A função
deve ignorar espaços antes e depois do nome e deve devolver o 
nome capitalizado, i.e., apenas com a 1ª letra maiuscula.
nomes = [Alice Miguel Sophia Arthur Helena Bernardo Valentina Heitor Laura Davi Isabella Lorenzo Manuela Théo Júlia Pedro]
"""

def mais_curto(lista_nomes):

    maior = 0

    for x in lista_nomes:
        if (maior < len(x.strip())):
            maior = len(x.strip())
            nome = x.strip()
    
    print("o Maior nome é %s e tem %d letras" %(nome.upper(), maior))






lista = ["   Alice ", " Miguel  ", "   Sophia " , "Arthur     ", " Helena", "Bernardo   ", "Valentina       ", 
"Heitor", " Laura ","Davi   ", "Isabella ", "Lorenzo ", "Manuela", "Théo", "Júlia", "Pedro"]
mais_curto(lista)
