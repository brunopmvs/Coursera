num = int(input("Infore um número: "))
divisor = 2


while(divisor <= num):
    multiplicidade = 0
    if(num % divisor == 0):
        while(num % divisor == 0):
            multiplicidade +=1
            num /= divisor
        print(divisor ,"^", multiplicidade)
    divisor +=1