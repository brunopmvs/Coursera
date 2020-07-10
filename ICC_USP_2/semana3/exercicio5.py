"""
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False.

Verifique a semelhança dos triângulos através do comprimento dos lados.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:
t1 = Triangulo(2, 2, 2)
t2 = Triangulo(4, 4, 4)
t1.semelhantes(t2)
# deve devolver True
"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def semelhantes(self, triangulo):
        
        t1 = [self.a, self.b, self.c]
        t1.sort()
        print(t1)
        t2 = [triangulo.a, triangulo.b, triangulo.c]
        t2.sort()
        print(t2)
        semelhantes = False
        razao = t1[0] / t2[0]
        if ( (t1[1] / t2[1] == razao) and (t1[2] / t2[2] == razao)):
            semelhantes = True
        
        return semelhantes

t1 = Triangulo(1, 2, 3)
t2 = Triangulo(2, 4, 6)
print(t1.semelhantes(t2))