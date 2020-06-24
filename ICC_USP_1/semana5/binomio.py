"""
O coeficiente binomial, também chamado de número binomial, de um número n, na classe k, consiste no número de combinações de n termos, k a k. 
O número binomial de um número n, na classe k, pode ser escrito como: 

n           n!
    =  ----------------
k        k!(n-k)!

lembrando: 
O fatorial de um número inteiro e positivo “n”, representado por “n!” é obtido a partir da multiplicação de todos os seus antecessores até o número um, 
cuja expressão genérica é n! = n . (n – 1). (n – 2). (n – 3) ... 2,1. 
• 3! = 3 . 2 . 1 = 6
• 4! = 4. 3 . 2 . 1 = 24
• 5! = 5 . 4 . 3 . 2 . 1 = 120


"""

def fatorial(x):
    fatorial = 1
    while(x > 1):
        fatorial *= x
        x-=1
    
    return fatorial

def numeroBinomial(n,k):
    return(  fatorial(n) / (fatorial(k)*fatorial(n-k)) ) 


n = int(input("Informe o valor de n: "))
k = int(input("Informe o valor de k: "))
print("O número binomial é ", numeroBinomial(n,k))



