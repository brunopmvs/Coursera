"""
Multiplica matrizes
"""
# def criaMatriz(iParam,jParam, valor = 0):
#     for i in range(iParam, jParam):
#         linha = []
#         for j in range(jParam):
#             linha.append()



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

def multiplicaMatrizes(m1, m2):

    result = []
    i_m1 = len(m1)
    j_m1 = len(m1[0])
    i_m2 = len(m2)
    j_m2 = len(m2[0])
    for i in range(i_m1):
        linha = []
        for j in range(j_m2):
            linha.append(m1[i][j] * m2[j][i])
            print(m1[i][j] * m2[j][i])
        result.append(linha)

    


    print(result)



m1 = [[2,5,9],[3,6,8]]
m2 = [ [2,7],[4,3],[5,2] ]

multiplicaMatrizes(m1, m2)
