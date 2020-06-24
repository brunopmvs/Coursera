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
rodada = 1


def partida():

    global player1Win
    global player2Win
    playerAtual = 3
    n = int(input("Informe o numero de peças: "))
    m = int(input("Informe o numero de peças a serem retiradas em cada jogada: "))
    playerInvalido = True

    while(playerInvalido):        
        
        playerAtual = int(input("Quem começa\nPlayer 1 - 1\nPlayer 2 - 2  "))

        if(playerAtual == 1 or playerAtual == 2):
            playerInvalido = False            
        else:
            print("Escolha novamente")
            playerInvalido = True

    while (n > 0):                              #pede a jogada
        if(playerAtual == 1):
            n -= player1Joga(n, m)
            playerAtual = 2
        else:            
            n -= player2Joga(n, m)
            playerAtual = 1

    if(playerAtual == 1):
        playerAtual = 2
        print("Player %d ganhou!" %(playerAtual))
        player2Win += 1
    else:
        playerAtual = 1
        print("Player %d ganhou!" %(playerAtual))
        player1Win += 1
            

def player1Joga(n, m):
    global playerAtual
    print("Restam %d peças no jogo" %(n))

    jogadaInvalida = True

    while(jogadaInvalida):
        jogada = int(input("Informe sua jogada (1): " ))
        if(jogada > m or jogada > n):
            print("Oops! Jogada inválida! Tente de novo.")
            jogadaInvalida = True
        else:
            jogadaInvalida = False

    
    #playerAtual = 2
    return jogada


def player2Joga(n, m):
    print("Restam %d peças no jogo" %(n))
    jogadaInvalida = True

    while(jogadaInvalida):
        jogada = int(input("Informe sua jogada (2): " ))
        if(jogada > m or jogada > n):
            print("Oops! Jogada inválida! Tente de novo.")
            jogadaInvalida = True
        else:
            jogadaInvalida = False

    return jogada
    #return jogada




print("Bem-vindo ao jogo do NIM! Escolha:\n\n")
jogadas = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

if (jogadas == 1):
    print("Voce escolheu uma partida isolada!")
    partida()
    print("Placar: Player 1 %d X %d Player 2" %(player1Win, player2Win))
else:
    jogadas = 0
    while (jogadas < 3):
        print("**** Rodada",jogadas,"****")
        partida()
        jogadas += 1
        print("**** Final do campeonato! ****\n\n")
        print("Placar: Player 1 %d X %d Player 2" %(player1Win, player2Win))
