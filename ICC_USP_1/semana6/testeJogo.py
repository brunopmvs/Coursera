"""
pergunta quantas peças e quantas peças por vez
pergunta ao usuario se vai ser 1 jogo ou 3
pede ao usuario 1 o n e o m
comeca a partida, com n peças
pede ao usuario 1 a jogada
pede ao usuario 2 a jogada

"""

def partida():
    if(jogadorAtual >0):
        print("Jogador : %d" %(jogadorAtual))

    if(n > 0):
        n -= usuario1_escolhe_jogada(n,mPecasARetirarPorJogada)
    else:  
        n -= usuario2_escolhe_jogada(n,mPecasARetirarPorJogada)

    print("Jogador %d venceu. Parabéns! " %(jogadorAtual))

def usuario1_escolhe_jogada(n, mPecasARetirarPorJogada):                                        

    jogadorAtual = 1
    jogadaUsuario = int(input("Informe sua jogada jogador %d: "%(jogadorAtual)))
    if(jogadaUsuario > mPecasARetirarPorJogada):
        print("Número de peças inválio, favor informar novamente com no máximo %d peças a retirar" %(mPecasARetirarPorJogada))
        usuario1_escolhe_jogada(n, mPecasARetirarPorJogada)
    else:
        return jogadaUsuario

def usuario2_escolhe_jogada(n, mPecasARetirarPorJogada):       #Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, 
                                        #solicita que o jogador informe sua jogada e verifica se o valor informado 
                                        # é válido. Se o valor informado for válido, a função deve devolvê-lo; 
                                        #caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

    jogadorAtual = 2
    jogadaUsuario = int(input("Informe sua jogada jogador %d: "%(jogadorAtual)))
    if(jogadaUsuario > mPecasARetirarPorJogada):
        print("Número de peças inválio, favor informar novamente com no máximo %d peças a retirar" %(mPecasARetirarPorJogada))
        usuario2_escolhe_jogada(n, mPecasARetirarPorJogada)
    else:
        return jogadaUsuario

n = 5 #int(input("Informe o numero de peças inicial: "))
mPecasARetirarPorJogada =0
mPecasARetirarPorJogada= int(input("Informe o numero de peças a ser retirado por jogada: "))
#jogadas = 0 
#jogadas = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
jogadorAtual = 4
print("Agora restam %d peças no tabuleiro." %(n))
partida()
