"""
pergunta quantas peças e quantas peças por vez
pergunta ao usuario se vai ser 1 jogo ou 3
pede ao usuario 1 o n e o m
comeca a partida, com n peças
pede ao usuario 1 a jogada
pede ao usuario 2 a jogada

n = numero de pecas no jogo
m = numero de peças a ser retirado em cada jogada
"""
player1Win = 0
player2Win = 0

def partida(n, m, playerAtual):
    while (n > 0):
        if(playerAtual == 1):
            n -= player1Joga(n, playerAtual, m)
            playerAtual = 2

        else:            
            n -= player2Joga(n, playerAtual, m)
            playerAtual = 1
    if(playerAtual == 1):
        playerAtual = 2
        print("Player %d ganhou!" %(playerAtual))
        player1Win +=1
    else:
        playerAtual = 1
        print("Player %d ganhou!" %(playerAtual))
        player2Win +=1
            

def player1Joga(n, playerAtual, m):
    print("Restam %d peças no jogo" %(n))
    jogada = int(input("Informe sua jogada player %d: " %(playerAtual)))
    while(jogada > m):
        print("Jogada inválida. Informe um número menor ou igual a %d" %(m))
        jogada = int(input("Informe sua jogada player %d: " %(playerAtual)))
    playerAtual = 2
    return jogada
    #return jogada


def player2Joga(n, playerAtual, m):
    print("Restam %d peças no jogo" %(n))
    jogada = int(input("Informe sua jogada player %d: " %(playerAtual)))
    while(jogada > m):
        print("Jogada inválida. Informe um número menor ou igual a %d" %(m))
        jogada = int(input("Informe sua jogada player %d: " %(playerAtual)))

    return jogada
    #return jogada

n = int(input("Informe o numero de peças: "))
m = int(input("Informe o numero de peças a serem retiradas em cada jogada: "))
playerAtual = 3

while(playerAtual > 2):
    playerAtual = int(input("Quem começa\nPlayer 1 - 1\nPlayer 2 - 2  "))


partida(n, m, playerAtual)