"""
Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos. Por exemplo, 120 é triangular, pois
 4 * 5 * 6
120
"""

num = int(input("Informe um número inteiro maior que 3: "))


dividendo = num
div1 = num + 1



while(div1 > 3):
    div1 -=1
    if( (dividendo % (div1) == 0 and dividendo % (div1-1) == 0 and dividendo % (div1-2) == 0) and num == (div1 * (div1-1) * (div1-2) )):
        print("O número é triangular. %d * %d * %d = %d" %(div1-2, div1-1, div1, num))
        break
    
else: 
    print("O número %d não é triangular" %(num))


"""if(div1 < 2):"""