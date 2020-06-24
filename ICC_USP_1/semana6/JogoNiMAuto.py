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
n = None
m = None

def partida():
    
    global player1Win
    global player2Win
    global n
    global m
    n = None
    m = None
    playerAtual = 3
    numeroPecasInvalido = True
    numeroPecasRetirarInvalido = True

    while(numeroPecasInvalido):   #pergunta quantas peças terá o tabuleiro
        
        if (n == None):
            n = int(input("Quantas peças? "))
        elif (n < 1):
            print("Número de peças inválido")
            n = int(input("Quantas peças? "))
            numeroPecasInvalido = True
        else:
            numeroPecasInvalido = False

    m = int(input("Limite de peças por jogada? "))

    # while(numeroPecasRetirarInvalido):     #pergunta quantas pecas poderão ser retiradas por jogada
    #     if (m == None):
    #         m = int(input("Limite de peças por jogada? "))
    #     elif(m < 1 or m > n):
    #         print("Número de peças inválido\n")
    #         m = int(input("Limite de peças por jogada? "))
    #         numeroPecasRetirarInvalido = True
    #     else:
    #         numeroPecasRetirarInvalido = False
            
 
    if ((n % (m+1)) == 0):
        print("Você começa")
        playerAtual = 1
    else:
        print("Computador começa!")
        playerAtual = 2



    while (n > 0):                      #pede a jogada
        if(playerAtual == 1):
            n -= usuario_escolhe_jogada(n, m)
            playerAtual = 2
        else:            
            n -= computador_escolhe_jogada(n, m)
            playerAtual = 1
    
    if (playerAtual == 2):
        player1Win += 1
    else:
        player2Win += 1
    print("Fim do jogo! O computador ganhou!") if (playerAtual == 1) else print("Fim do jogo! Você ganhou!")
    
     

def usuario_escolhe_jogada(n, m):

    print("Agora restam %d peças no tabuleiro." %(n))

    jogadaInvalida = True

    while(jogadaInvalida):
        
        jogada = int(input("Quantas peças você vai tirar? " ))
        
        if(jogada > m or jogada > n or jogada < 0):
            print("Oops! Jogada inválida! Tente de novo.")
            jogadaInvalida = True
        
        else:
            jogadaInvalida = False
    return jogada


def computador_escolhe_jogada(n, m):
    #Estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. 
    #Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
    print("Agora restam %d peças no tabuleiro." %(n))

    jogada = (n%(m+1))
    if(jogada == 0 and n > m+1):
        jogada = m
    print("O computador tirou", "uma peça." if (jogada == 1) else  "%d peças" %(jogada))

    
    return jogada



print("Bem-vindo ao jogo do NIM!\nEscolha:\n")
jogadas = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

if (jogadas == 1):
    print("Voce escolheu uma partida isolada!")
    partida()
    print("Placar: Você %d X %d Computador" %(player1Win, player2Win))
else:
    jogadas = 1
    while (jogadas <= 3):
        print("Voce escolheu um campeonato!")
        print("**** Rodada",jogadas,"****")
        partida()
        jogadas += 1
        print("**** Final do campeonato! ****\n\n")
        print("Placar: Você %d X %d Computador" %(player1Win, player2Win))
