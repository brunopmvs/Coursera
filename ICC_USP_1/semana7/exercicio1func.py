def fatorial(x):
    fatorial = 1
    while(x > 1):
        fatorial *= x
        x -= 1
    
    return fatorial

calcula = True

while(calcula):
    
    x = int(input("Informe o número para calcular o fatorial: "))
    
    print("Fatorial de %d é : %d"%(x,fatorial(x)))
    
    n = input("Digite X para sair, ou qualquer outro valor para continuar \n")
    if(n == "X" or n =="x"):
        calcula = False