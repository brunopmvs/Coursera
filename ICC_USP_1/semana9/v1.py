"""
Concluindo

Basicamente, sua tarefa é implementar corretamente as seguintes funções:

    compara_assinatura(as_a, as_b)
    calcula_assinatura(texto)
    avalia_textos(textos, ass_cp)
    Um passo importante para seu programa é calcular a assinatura dos textos corretamente. 
    Para testar se sua função calcula_assinatura() está correta, deixamos aqui um exemplo de execução:

    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
calcula_assinatura(texto)
>[5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]


    """
import re

def separa_PalavrasTexto(texto):
    # Texto > Sentenças > Frases > Palavras
    #Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
   
    # PASSO 1 - Separar o texto em sentenças
    sentencas = separa_sentencas(texto)
    numeroSentencas = len(sentencas)

    # PASSO 2 - Separas as sentenças em frases
    frases = []
    for x in sentencas:
        for i in separa_frases(x):
            frases.append(i)
    # frases = []
    # frases = separa_frases(texto) 
    numeroFrases = len(frases)
    print(numeroFrases)

    # PASSO 3 - Separar as frases em palavras

    palavras = []
    for x in frases:
        for i in separa_palavras(x):
            palavras.append(i)

    numeroPalavras = len(palavras)
    return [palavras, numeroSentencas, numeroFrases, numeroPalavras]

def calcula_TamanhoMedioPalavras(listaPalavras):
    """A função recebe uma lista de palavras e retorna o tamanho médio delas """
    tamanhoMedioPalavra = 0.0
    somaTamanhoPalavras = 0

    for x in listaPalavras:
        print((x))
        #somaTamanhoPalavras += len(x)
 

    tamanhoMedioPalavra = (somaTamanhoPalavras/len(listaPalavras))

    return tamanhoMedioPalavra

def calcula_RelacaoTypeToken(lista_palavras):
    """Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. """
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) 
    # mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4 / 5 = 0.8
    
    numeroPalavrasTexto = len(lista_palavras)
    nPalavrasDiferentes = n_palavras_diferentes(lista_palavras)
    return (nPalavrasDiferentes / numeroPalavrasTexto) # relacao Type Token

def calcula_RazaoHapaxLegomana(lista_palavras):
    """ Razão Hapax Legomana é o número de palavras que aparecem uma única vez
     dividido pelo total de palavras. """
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total 
    # (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez 
    # (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 3 / 5 = 0.6
    
    numeroPalavrasTexto = len(lista_palavras)
    npalavrasUnicas = n_palavras_unicas(lista_palavras)
    return (npalavrasUnicas / numeroPalavrasTexto)    #razao Hapax Legomana

def calcula_TamanhoMedioSentenca(texto):
    """Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças""" 
    #(os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    
    somaCaracteres = 0
    lista = separa_sentencas(texto)

    for x in lista:
        somaCaracteres += len(x)
    
    return somaCaracteres / len(lista)

def calculaComplexidadeSentenca(numeroFrases, numeroSentencas):
    """Calcula número total de frases divido pelo número de sentenças."""
    return numeroFrases / numeroSentencas

def calculaTamanhoMedioFrase(texto):
    """Calcula a soma do número de caracteres em cada frase dividida pelo número de frases no texto"""
    # (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

    somaCaracteres = 0
    sentencas = separa_sentencas(texto)

    frases = []
    for x in sentencas:
        for i in separa_frases(x):
            frases.append(i)
            somaCaracteres += len(i)

    return somaCaracteres / len(frases)


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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    
    retornoTextoSeparado = separa_PalavrasTexto(texto)
    listaPalavras = separa_PalavrasTexto(texto)
    tamanhoMedioPalavra = calcula_TamanhoMedioPalavras(listaPalavras)
    relacaoTypeToken = calcula_RelacaoTypeToken(listaPalavras)
    razaoHapaxLegomana = calcula_RazaoHapaxLegomana(listaPalavras)
    tamanhoMedioSentenca = calcula_TamanhoMedioSentenca(texto)
    complexidadeMediaSentenca = calculaComplexidadeSentenca(retornoTextoSeparado[2], retornoTextoSeparado[1])
    tamanhoMedioFrase = calculaTamanhoMedioFrase(texto)
    numeroPalavras = retornoTextoSeparado[3]

    return [tamanhoMedioPalavra, relacaoTypeToken, razaoHapaxLegomana,tamanhoMedioSentenca, complexidadeMediaSentenca, tamanhoMedioFrase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


#texto = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
# texto = "Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso. Quero para mim o espírito esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade; ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."

# retornoTextoSeparado = separa_PalavrasTexto(texto)
# palavrasTexto = retornoTextoSeparado[0]
# numeroSentencasTexto = retornoTextoSeparado[1]
# numeroFrasesTexto = retornoTextoSeparado[2]
# numeroPalavrasTexto = retornoTextoSeparado[3]
# print("Número de Sentenças no texto = ", numeroSentencasTexto)
# print("Número de Frases no texto = ", numeroFrasesTexto)
# print("Numero de Palavras no texto = ", numeroPalavrasTexto)
# print("Tamanho médio de palavra: ", calcula_TamanhoMedioPalavras(palavrasTexto))
# print("Relação Type Token: ", calcula_RelacaoTypeToken(palavrasTexto))
# print("Razão Hapax Legomana :", calcula_RazaoHapaxLegomana(palavrasTexto))
# print("Tamanho médio de sentença : ", calcula_TamanhoMedioSentenca(texto))
# print("Complexidade de sentença: ", calculaComplexidadeSentenca(numeroFrasesTexto, numeroSentencasTexto))
# print("Tamanho médio de frase REF (45.888888888888886) = ", calculaTamanhoMedioFrase(texto))

calcula_assinatura(texto)

#print(separa_frases("Quero para mim o espírito esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar"))

# le_assinatura()
# le_textos()