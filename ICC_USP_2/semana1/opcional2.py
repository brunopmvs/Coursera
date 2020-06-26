"""
Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao
 número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que 
 recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis 
 (na ordem dada) e False caso contrário.

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) => False

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) => True

Testes:
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))


m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))

"""


def sao_multiplicaveis(m1, m2):

    i_m1 = 0
    j_m1 = 0
    i_m2 = 0
    j_m2 = 0

    if( (len(m1) == 1) and (len(m2) == 1)):
        #return True
        print(True)

    if( len(m1) == 1 and type(m1[0] == int)):
        i_m1 = 1
        j_m1 = 1
    elif (len(m1) == 1):
        i_m1 = 1
        for j in m1[0]:
            j_m1 += 1
    elif( (len(m1) > 1) and type(m1[0] == int)):
        j_m1 = 1
        for j in m1:
            i_m1 += 1
    
    if( len(m2) == 1 and type(m2[0] == int)):
        i_m2 = 1
        j_m2 = 1
    elif(len(m2) == 1):
        i_m2 = 1
        for j in m2[0]:
            j_m2 += 1
    elif( (len(m2) > 1) and type(m2[0] == int)):
        j_m2 = 1
        for j in m2:
            i_m2 += 1

    if(i_m1 == j_m2):
        return True
    else:
        return False



m1 = [1]
m2 = [1,3,3]
print(sao_multiplicaveis(m1,m2))

    
