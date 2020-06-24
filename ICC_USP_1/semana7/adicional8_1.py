"""Exercício 8.1

Nota: Questão 1 da Prova 1 de 2014.

Na figura, no plano cartesiano, a região sombreada não inclui as linhas de bordo. Note que o eixo y cai bem no meio da figura, e usamos o lado do quadrado para indicar as ordenadas correspondentes.

Escreva na página do desenho um programa que lê as coordenadas cartesianas (x, y) de um ponto, ambas do tipo float e imprime dentro se esse ponto está na região, e fora caso contrário.

8    ##########
7    #   ##   #
6    # # ## # #
5    #   ##   #
4    ##########
3    ##########
2    ##      ##
1    ##      ##
0    ##########
    -5        5
"""
dentro = False
y = 0
x = 0
matriz =[]
matriz.append("##########")
matriz.append("#000##000#")
matriz.append("#0#0##0#0#")
matriz.append("#000##000#")
matriz.append("##########")
matriz.append("##########")
matriz.append("##000000##")
matriz.append("##########")


xprocurado = (5 + float(input("Informe a valor de X do ponto procurado: ")))   # 5 para ajustar aos valores negativos do plano 
yprocurado = (float(input("Informe a valor de Y do ponto procurado: ")))
print(xprocurado,yprocurado)
while(y < 8):
    
    while(x < 10):
        #print(matriz[y][x], end="")
        selecionado = matriz[y][x]
        if( ((selecionado == "0") and (xprocurado > x) and (yprocurado > y) and (x < 5)) or ((selecionado == "0") and (xprocurado < x) and (yprocurado < y) and (x > 5)) ):
            #print("Dentro")
            print("x = %d  e y = %d , %s" %(x, y, selecionado))
            dentro = True
            break

        x += 1
    y += 1
    x = 0

print("Dentro!") if dentro else print("Fora!")