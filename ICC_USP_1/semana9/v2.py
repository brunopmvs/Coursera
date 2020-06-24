import re

texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
texto1="Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso. Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
texto2="Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
texto3="NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''


    walA = as_a[0]  #tamanho médio de palavra
    ttrA = as_a[1]  #relação Type-Token
    hlrA = as_a[2]  #Razão Hapax Legomana
    salA = as_a[3]  #tamanho médio de sentença
    sacA = as_a[4]  #complexidade média da sentença
    palA = as_a[5]  #tamanho medio de frase
        
    walB = as_b[0]  #tamanho médio de palavra
    ttrB = as_b[1]  #relação Type-Token
    hlrB = as_b[2]  #Razão Hapax Legomana
    salB = as_b[3]  #tamanho médio de sentença
    sacB = as_b[4]  #complexidade média da sentença
    palB = as_b[5]  #tamanho medio de frase
    

    wal = abs(walA-walB)
    ttr = abs(ttrA-ttrB)
    hlr = abs(hlrA-hlrB)
    sal = abs(salA-salB)
    sac = abs(sacA-sacB)
    pal = abs(palA-palB)
    
    sAB = (wal + ttr + hlr + sal + sac + pal) / 6 #grau de similaridade

    return sAB
    
def calcula_assinatura(texto):
    
    listaSentencasTexto = separaSentencasTexto(texto)
    listaFrasesTexto = separaFrasesLista(listaSentencasTexto)
    listaPalavrasTexto = separaPalavrasLista(listaFrasesTexto)



    tamanhoMedioPalavra = calculaTamanhoMedioPalavra(listaPalavrasTexto)
    relacaoTypeToken = calculaRelacaoTypeToken(listaPalavrasTexto)
    razaoHapaxLegomana = calculaRazaoHapaxLegomana(listaPalavrasTexto)
    tamanhoMedioSentenca = calculaTamanhoMedioSentenca(listaSentencasTexto)
    complexidadeMediaSentenca = calculaComplexidadeSentenca(listaFrasesTexto, listaSentencasTexto)
    tamanhoMedioFrase = calculaTamanhoMedioFrase(listaFrasesTexto)




    return[tamanhoMedioPalavra, relacaoTypeToken, razaoHapaxLegomana, tamanhoMedioSentenca, complexidadeMediaSentenca, tamanhoMedioFrase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    lista = []
    i = 0
    nRetornar = 0
    maior_sAB = 0


    for x in textos:
        assinatura = calcula_assinatura(x)
        sAB = compara_assinatura(ass_cp, assinatura) #grau de similaridade
        lista.append([i, x, assinatura, sAB])
        i += 1 

    for x in lista:
        if(maior_sAB < x[3]):
            maior_sAB = x[3]
            nRetornar = x[0]
    
    return(nRetornar)




def separaSentencasTexto(texto):
    
    listaSentencas = []
   
    listaSentencas = separa_sentencas(texto)
    
    return listaSentencas

def separaFrasesLista(listaSentencas):

    listaFrases = []

    for x in listaSentencas:
        listaFrases.extend(separa_frases(x))

    return listaFrases

def separaPalavrasLista(ListaFrases):

    listaPalavras = []

    for x in ListaFrases:
        listaPalavras.extend(separa_palavras(x))

    return listaPalavras

def calculaTamanhoMedioPalavra(listaPalavras):
    """Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras."""
    somaTamanhoPalavras = 0
    
    for x in listaPalavras:
        somaTamanhoPalavras += len(x)
    return somaTamanhoPalavras / len(listaPalavras)

def calculaRelacaoTypeToken(listaPalavras):
    """Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. """
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) 
    # mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4 / 5 = 0.8
    
    numeroPalavrasTexto = len(listaPalavras)
    nPalavrasDiferentes = n_palavras_diferentes(listaPalavras)
    return (nPalavrasDiferentes / numeroPalavrasTexto) # relacao Type Token

def calculaRazaoHapaxLegomana(listaPalavras):
    """ Razão Hapax Legomana é o número de palavras que aparecem uma única vez
     dividido pelo total de palavras. """
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total 
    # (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez 
    # (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 3 / 5 = 0.6
    
    numeroPalavrasTexto = len(listaPalavras)
    npalavrasUnicas = n_palavras_unicas(listaPalavras)
    return (npalavrasUnicas / numeroPalavrasTexto)    #razao Hapax Legomana

def calculaTamanhoMedioSentenca(listaSentencas):
    """Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças""" 
    #(os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    
    somaTamanhoSentencas = 0
    
    for x in listaSentencas:
        somaTamanhoSentencas += len(x)
    
    return somaTamanhoSentencas / len(listaSentencas)

def calculaComplexidadeSentenca(listaFrases, listaSentencas):
    """Calcula número total de frases divido pelo número de sentenças."""
    return len(listaFrases) / len(listaSentencas)

def calculaTamanhoMedioFrase(listaFrases):
    """Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto"""
    #(os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
    
    somaTamanhoFrases = 0
    
    for x in listaFrases:
        somaTamanhoFrases += len(x)
    
    return somaTamanhoFrases / len(listaFrases)

##textoRef = texto
##listaPalavrasTexto = separaPalavrasLista(separaFrasesLista(separaSentencasTexto(textoRef)))
##print(calcula_assinatura(textoRef))

#calcula_assinatura(texto)
###print([5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886])
#print(avalia_textos(le_textos(), le_assinatura()))
# compara_assinatura(calcula_assinatura(texto1), calcula_assinatura(texto2))

#(avalia_textos([texto1,texto2,texto3],assinatura))