def ePrimo(x):

    divisor = x
    primo = True

    while (divisor > 2):
        divisor -= 1
        if x % divisor == 0:
            primo = False
            break
        else:
            primo = True

    return primo    


num = int(input("Infore um número: "))
divisor = 2


while(divisor <= num):
    multiplicidade = 0
    if(ePrimo(divisor) and num % divisor == 0):
        while(num % divisor == 0):
            multiplicidade +=1
            num /= divisor
        print(divisor ,"^", multiplicidade)
    divisor +=1