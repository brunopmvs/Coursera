"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:
digite a largura: 10
digite a altura: 3
##########
#        #
##########
digite a largura: 2
digite a altura: 2
##
##
"""
largura = int (input("digite a largura:"))
altura = int(input("digite a altura:"))
alt = altura


while(alt > 0):
    larg = largura
    while(larg > 0):
        if((larg == largura or larg == 1) or (alt == 1 or alt == altura)):
            print("#", end = "")
        
        else:
            print(" ", end = "")
        larg -=1
    print("")
    alt -=1